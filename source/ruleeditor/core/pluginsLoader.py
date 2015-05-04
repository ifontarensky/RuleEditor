


"""The plugins loader module.

Every module under the plugins directory is a plugin.
This module finds, loads, instantiates and registers the available plugins.

There are (at least) 2 approaches for loading the plugins under
the plugins directory:

a) to iterate over a list of module names
b) to iterate over the content of the plugins directory

Syntax of a) is simpler (see below) but b) seems to be more general and
powerful as it can deal with packages too. So *at the moment* I'll use the
approach b). In the future a better defined plugins infrastructure may be used.

FYI, approach a) looks like::

    from vitables.plugins import __all__ as plugins
    for plugin in plugins:
        try:
            module_name = 'vitables.plugins.' + plugin
            __import__(module_name)
            module = sys.modules[module_name]
        except ImportError:
            print "Error: module %s cannot be loaded" % module_name
"""

__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'

import sys
import os
import pkgutil
import imp

from PyQt4 import QtGui

from ruleeditor.reconstant import PLUGINSDIR

import ruleeditor.plugins

translate = QtGui.QApplication.translate

def isPlugin(folder, name):
    """Check if a given module is a plugin.

    :Parameters:
        - folder: the folder where the module being tested lives
        - name: the filename of the module being tested
    """
    # Import the module
    try:
        finding_failed = True
        file_obj, filepath, desc = imp.find_module(name, [folder])
        finding_failed = False
#        module = imp.load_module(name, file_obj, filepath, desc)
        module = imp.load_source(name, filepath, file_obj)
    except (ImportError, Exception) as e:
        print e
        # Warning! If the module being loaded is not a ViTables plugin
        # then unexpected errors can occur
        return False
    finally:
        if not finding_failed:
            file_obj.close()

    # Check if module is a plugin
    try:
        class_name = getattr(module, 'plugin_class')
        return class_name
    except AttributeError:
        return False

    #######################################################
    #
    # WARNING!!! DO NOT DELETE MODULES AFTER CHECKING
    #
    # Deletion has unwanted side effects. For instance,
    # deleting the time_series module results in deleting
    # the tables module!!!
    #
    #######################################################

    # finally:
        # path = '%s.py' % os.path.join(folder, name)
        # modname = inspect.getmodulename(path)
        # del sys.modules[modname]
        # del module


def scanFolder(folder):
    """Scan a package looking for plugins.

    This is a non recursive method. It scans only the top level of
    the package.

    :Parameter folder: the folder being scanned
    """


    pkg_plugins = []
    for loader, name, ispkg in pkgutil.iter_modules([folder]):
        if not ispkg and isPlugin(folder, name):
            pkg_plugins.append(u'{0}#@#{1}'.format(folder, name))
    return pkg_plugins


class PluginsLoader(object):
    """Plugins loader class.

    Every module|package under the plugins directory is a plugin. At the
    moment packages can contain module plugins only at top level because
    the plugins manager doesn't iterate recursively over the package looking
    for plugins.

    :Parameters:

    - plugins_paths: a list with the paths where plugins live
    - enabled_plugins: a list with the UIDs of the enabled plugins
    """

    def __init__(self, plugins_paths, enabled_plugins):
        """Dynamically load and instantiate the available plugins.
        """

        self.plugins_paths = plugins_paths[:]
        self.enabled_plugins = enabled_plugins[:]


        # Ensure that plugins distributed along with ViTables are
        # always available
        if PLUGINSDIR not in self.plugins_paths:
            self.plugins_paths.append(PLUGINSDIR)
            self.enabled_plugins.append(PLUGINSDIR)

        # Make sure that other plugins (if any) are available
        for path in self.plugins_paths:
            if os.path.isabs(path) and (path not in sys.path):
                sys.path = [path] + sys.path

        # Some useful stuff
        self.all_plugins = []
        self.disabled_plugins = []
        self.loaded_plugins = {}

        # Update plugins information: available plugins, disabled plugins
        self.register()


    def register(self):
        """Update the lists of available/enabled/disabled plugins.

        This method MUST be called every time that the plugins
        configuration changes.
        """

        # Setup the list of available plugins
        self.all_plugins = []
        for folder in self.plugins_paths:
            for loader, name, ispkg in pkgutil.iter_modules([folder]):
                if not ispkg and isPlugin(folder, name):
                    self.all_plugins.append(u'{0}#@#{1}'.format(folder, name))
                else:
                    pkg_plugins = scanFolder(os.path.join(folder, name))
                    self.all_plugins = self.all_plugins + pkg_plugins
                    # /!\ FIX : TOREMOVE
                    self.enabled_plugins = self.all_plugins

        # Make sure that enabled plugins are included in the list of
        # available plugins (sometimes this is required. When it is not
        # doing it is harmless)
        for enabled in self.enabled_plugins:
            if enabled not in self.all_plugins:
                self.all_plugins.append(enabled)

        # Setup the list of disabled plugins
        self.disabled_plugins = [plugin for plugin in self.all_plugins \
            if plugin not in self.enabled_plugins]


    def loadAll(self):
        """Try to load the enabled plugins.
        """
        if self.enabled_plugins == []:
            return
        for plugin in self.enabled_plugins:
            self.load(plugin)


    def load(self, plugin):
        """Load a given plugin.

        :Parameters plugin: th UID of the plugin being loaded
        """

        # Load the module where the plugin lives
        try:
            finding_failed = True
            (folder, name) = plugin.split('#@#')
            file_obj, filepath, desc = imp.find_module(name, [folder])
            finding_failed = False
    #        module = imp.load_module(name, file_obj, filepath, desc)
            module = imp.load_source(name, filepath, file_obj)
        except (ImportError, ValueError):
            self.untrack(plugin)
            if finding_failed:
                print(u"\nError: plugin {0} cannot be found.".format(plugin))
            else:
                print(u"\nError: plugin {0} cannot be loaded.".format(name))
            return
        except Exception as error:
            print error
        finally:
            if not finding_failed:
                file_obj.close()

        # Retrieve the plugin class
        try:
            class_name = getattr(module, 'plugin_class')
            cls = getattr(module, class_name)
        except AttributeError:
            self.untrack(plugin)
            print(u"\nError: module {0} is not a valid plugin.".format(name))
            return

        # Load the plugin
        try:
            instance = cls()

            # Register plugin
            # In some cases keeping a reference to instance is a must
            # (for example, the time_series plugin)
            self.loaded_plugins[plugin] = instance
            print(u" * Plugin Loaded : {0} ({1})".format(name, class_name))
        except Exception as error:
            self.untrack(plugin)
            print(u"\nError: plugin {0} cannot be loaded.".format(name))
            print(u"  + {0}".format(error))
            return


    def untrack(self, plugin):
        """Remove a plugin from the lists of available/enabled plugins.

        Plugins that cannot be loaded should be removed using this method.

        :Parameter plugin: the plugin being removed
        """

        try:
            self.all_plugins.remove(plugin)
            self.enabled_plugins.remove(plugin)
        except IndexError:
            pass

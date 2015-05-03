
rule apt_demo {
	meta:
		description = "This Yara contains indicators detailed in the blog post 'demo'"
		author = "Ivan"
		reference = "http://www.demo.com/demo.html"
	strings:
		$filepath = "LOCAL SETTINGS\Temp" ascii


	condition:
		all of the
}

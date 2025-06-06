spec_content = """
[app]
title = HelloWorld
package.name = helloworld
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.0.0

[buildozer]
log_level = 2
warn_on_root = 1
"""

with open("buildozer.spec", "w", encoding="utf-8") as f:
    f.write(spec_content.strip())

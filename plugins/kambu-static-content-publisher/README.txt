Kambu Static Content Publisher

This plugin publishes the bundled HTML guides as ordinary WordPress posts or pages while rendering the source files directly at the_content priority 99. Gutenberg, wpautop and post-content formatting do not rewrite the rendered HTML.

Install
1. Zip the kambu-static-content-publisher folder.
2. Upload it at Plugins > Add New > Upload Plugin.
3. Activate it.
4. Open Tools > Kambu Static Publisher.
5. Choose Post or Page for each file.
6. Sync as drafts first. Review the staging output, then sync as published when approved.

The bundled files are listed in manifest.json and live in content/. Each imported item stores its source filename in _kambu_static_source and uses the Essential Blocks Fullwidth Template when that template is available.

The plugin does not delete existing posts or pages. Re-syncing updates the item that owns the same source filename.

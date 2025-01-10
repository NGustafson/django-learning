# Djabricator
My Homage to Phabricator in Django and TailwindCSS


## Development
### TailwindCSS Setup
1. Download the latest [release](https://github.com/tailwindlabs/tailwindcss/releases), and place it in this directory.
2. Run the following command to automatically update `output.css` when new classes are used `./tailwindcss -i ./projects/static/css/input.css -o ./projects/static/css/output.css --watch`
3. Include `output.css` in template files to apply.

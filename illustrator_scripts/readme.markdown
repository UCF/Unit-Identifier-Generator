# Generate Unit Identifiers using Illustrator

## Setup Illustrator
1. Open Illustrator
1. Open actions window and load unit-id.aia action
1. Copy Unit-ID-Generator.js file to /Illustrator CC/Presets/en_US/Scripts folder
1. Restart Illustrator

## Create EPS files
1. Open Illustrator
1. Open image unit-id.ai
1. Open variables window and load unit-id-variables.xml, located under the variable window menu
1. Run the "Save as EPS" action as a batch, located under the actions window menu
1. Batch settings should look similar to the batch-settings.png image
1. EPS versions of the unit identifier are generated in the folder you specified

## Create PNG and PDF files
1. Select File -> Scripts -> Unit ID Generator
1. PNG and PDF images are generated and copied into new unit id folders allong with the EPS file
# Generate Unit Identifiers using Illustrator

1. Open Illustrator
1. Open actions window and load unit-id.aia action
1. Open image unit-id.ai
1. Open variables window and load unit-id-variables.xml, located under the variable window menu
1. Run the "Save as EPS" action as a batch, located under the actions window menu
1. Batch settings should look similar to the batch-settings.png image
1. Set the destination to the output folder relative to the unit-id.js script
1. EPS versions of the unit identifier are generated in the output folder (Two are generated, not sure why?)
1. rm -rf *-01.eps to remove the extra EPS files
1. Select the file menu -> Scripts -> Other Scripts option and select the unit-id.js file
1. PNG and PSD versions are generated in the output folder

Ideally this would be a one step process using the batch functionality or a JS script
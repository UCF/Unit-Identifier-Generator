// uncomment to suppress Illustrator warning dialogs
// app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;

var sourceFolder,
    files,
    targetFile;

// Select the source folder.
sourceFolder = Folder.selectDialog('Select the folder with EPS files to convert', '~');

// If a valid folder is selected
if (sourceFolder !== null) {
    files = [];

    // Get all files matching the pattern
    files = sourceFolder.getFiles('*.eps');

    if (files.length > 0) {
        // Get the destination to save the files
        for (i = 0; i < files.length; i++) {
            var sourceDoc = app.open(files[i]),
                originalName = sourceDoc.name,
                newName = sourceDoc.name.split('_')[1].split('.')[0],
                newFolder = new Folder(sourceDoc.path + '/' + newName).create(),
                destFolder = sourceDoc.path + '/' + newName + '/';

            // Export PNG
            targetFile = new File(destFolder + '/' + sourceDoc.name.split('.')[0] + '.png');
            sourceDoc.exportFile(targetFile, ExportType.PNG24, getPNGOptions());

            // Export PDF
            targetFile = new File(destFolder + '/' + sourceDoc.name.split('.')[0] + '.pdf');
            sourceDoc.saveAs(targetFile, getPDFOptions());

            if (files[i].copy(destFolder + originalName)) {
                files[i].remove();
            }

            sourceDoc.close(SaveOptions.DONOTSAVECHANGES);
        }
        alert('Files have been saved as PNG and PDF files');
    }
    else {
        alert('No matching files found');
    }
}


/** Returns the options to be used for the generated files.
  @return PDFSaveOptions object
*/
function getPDFOptions() {
    var options = new PDFSaveOptions();
    options.compatibility = PDFCompatibility.ACROBAT5;
    options.generateThumbnails = false;
    options.preserveEditability = true;
    return options;
}


/** Returns the options to be used for the generated files.
  @return ExportOptionsPNG24 object
*/
function getPNGOptions() {
    var options = new ExportOptionsPNG24();
    options.antiAliasing = true;
    options.artBoardClipping = false;
    // options.horizontalScale = 250.0;
    //options.matte = true;
    //options.matteColor = 0, 0, 0;
    options.saveAsHTML = false;
    options.transparency = true;
    // options.verticalScale = 250.0;
    return options;
}
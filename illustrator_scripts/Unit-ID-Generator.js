// uncomment to suppress Illustrator warning dialogs
// app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;

var sourceFolder, files, sourceDoc, targetFile;

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
            sourceDoc = app.open(files[i]);

            // Export PNG
            targetFile = new File(sourceDoc.path + '/' + sourceDoc.name.replace('.eps', '.png'));
            sourceDoc.exportFile(targetFile, ExportType.PNG24, getPNGOptions());

            // Export PDF
            targetFile = new File(sourceDoc.path + "/" + sourceDoc.name.replace('.eps', '.pdf'));
            sourceDoc.saveAs(targetFile, getPDFOptions());

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
// uncomment to suppress Illustrator warning dialogs
// app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;

var sourceFolder, folders, files, sourceDoc, targetFile;

// Select the source folder.
// sourceFolder = Folder.selectDialog('Select the folder with EPS files to convert', '~');
sourceFolder = Folder('~/Projects/Unit-Identifier-Generator/src/illustrator_scripts/output');

// If a valid folder is selected
if (sourceFolder !== null) {
    files = [];
    folders = [];

    folders = sourceFolder.getFiles();

    if (folders.length > 0) {

        // alert(folders);
        // Get the destination to save the files
        for (var i = 0; i < folders.length; i++) {
            if (!folders[i].toString().match(/\.DS_Store|\.BridgeSort/g)) {
                alert(folders[i]);

                // Get all files matching the pattern
                files = Folder(folders[i]).getFiles('*.eps');

                if (files.length > 0) {
                    // Get the destination to save the files
                    for (var j = 0; j < files.length; j++) {
                        sourceDoc = app.open(files[j]);

                        var newName = sourceDoc.name.replace('.eps', '');
                        // Export PNG
                        targetFile = new File(sourceDoc.path + '/' + newName + '.png');
                        sourceDoc.exportFile(targetFile, ExportType.PNG24, getPNGOptions());

                        // Export PDF
                        targetFile = new File(sourceDoc.path + "/" + newName + '.pdf');
                        sourceDoc.saveAs(targetFile, getPDFOptions());

                        sourceDoc.close(SaveOptions.DONOTSAVECHANGES);
                    }
                } else {
                    alert('No matching files found');
                }
            }
        }
        alert('Files have been saved as PNG and PDF files');
    } else {
        alert('No folders found');
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
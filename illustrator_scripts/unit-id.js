
// suppress Illustrator warning dialogs
app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;

var doc = app.activeDocument,
    dataSets = doc.dataSets,
    filesNames = [];

for (var i = 0; i < dataSets.length; i++) {
    var set = dataSets[i];
    set.display();

    doc.exportFile(getNewName(doc, set.name + '.png'), ExportType.PNG24, getPNGOptions());

    doc.exportFile(getNewName(doc, set.name + '.psd'), ExportType.PHOTOSHOP, getPSDOptions());
}


/** Returns new filename.
  @return File object
*/
function getNewName(doc, ext) {
    var docName, newName, saveInFile;
    docName = doc.name;
    newName = "";

    for (var i = 0; docName[i] != "."; i++) {
        newName += docName[i];
    }
    newName += ext; // full png name of the file

    // Create a file object to save the png
    saveInFile = new File(doc.path + '/output/' + ext);

    return saveInFile;
}


/** Returns the options to be used for the generated files.
  @return ExportOptionsPNG24 object
*/
function getPNGOptions() {
    var pngExportOpts = new ExportOptionsPNG24();
    pngExportOpts.antiAliasing = true;
    pngExportOpts.artBoardClipping = true;
    pngExportOpts.horizontalScale = 250.0;
    //pngExportOpts.matte = true;
    //pngExportOpts.matteColor = 0, 0, 0;
    pngExportOpts.saveAsHTML = false;
    pngExportOpts.transparency = true;
    pngExportOpts.verticalScale = 250.0;
    return pngExportOpts;
}

/** Returns the options to be used for the generated files.
  @return ExportOptionsPhotoshop object
*/
function getPSDOptions() {
    var options = new ExportOptionsPhotoshop();
    options.resolution = 150;
    options.saveMultipleArtboards = true;
    return options;
}
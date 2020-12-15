$(function(){
    var editor = CodeMirror.fromTextArea(document.getElementById('editor_input'), {
        mode: "javascript",
        theme: "dracula",
        lineNumbers: true,
        matchBrackets: true,
        autoCloseBrackets: true,
    });
    editor.setSize("90%", "90%");

    var output = CodeMirror.fromTextArea(document.getElementById('editor_output'), {
        mode: "javascript",
        theme: "dracula",
        lineNumbers: true,
        matchBrackets: true,
        autoCloseBrackets: true,
        //readOnly: true,
    });
    output.setSize("90%", "90%");

    
});

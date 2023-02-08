console.log("Load Successful.");
var logs = [
    "[INFO]Waiting server response...",
    "[WARNNIG]No response.",
    "[INFO]"
];
var logstart = $("#b_logstart");
var terminal = $("#terminal");
console.log(logstart);

function nowTime() {
    var now = new Date();
    return (now.getHours() +":"+ now.getMinutes() +":"+ now.getSeconds());
}

console.log("...");
function addlog(string) {
    terminal.append("<span>" + string + "</span>");
}

logstart.onclick = function (e) {
    e.preventDefault();
    console.log("Excuting...");
    logstart.hide();
    addlog("  ####   ####   ____        W");
    addlog(" /      /      /  W *  W    W");
    addlog(" -555   -55+   0   W * W   W");
    addlog("    ==     =++ 0    0/W W W");
    addlog("HUMAN  ALWAYS +-WIN-+W   W");
    addlog("");
    addlog("INTELLIGENT QUANTUM COMPUTER 550W (MOSS)");
    addlog("Copyright 2012-2077 United Earth Government.");

    addlog("Generating root Opearing System...");
    while (true) {
        var log = "[" + nowTime() + "]" + text;
        addlog(log);
    }
}

console.log("JavaScript file finished.");
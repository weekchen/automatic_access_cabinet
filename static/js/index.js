function go_out() {
    document.getElementById("iframe_a").src = "take_out.html"
}

function go_in() {
    document.getElementById("iframe_a").src = "take_in.html"
}

function change_frame() {
    document.getElementById("iframe_a").src = "welcome.html"
    // window.top.location.reload()
    // document.getElementById('iframe_a').contentWindow.location.reload(true)
}

// function take_out(num) {
//     alert("货物已存入")
//     document.getElementById(num).style.background = "red"
//     go_back()
// }
//
// function go_back() {
//     // self.parent.document.getElementById("iframe_a").src = "welcome.html"
//     // alert(self.parent.document.getElementById("iframe_a").src)
//     // self.parent.parent.location.reload()
// }
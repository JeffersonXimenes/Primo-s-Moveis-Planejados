function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "0px";
    document.getElementById("full").style.marginLeft = "250px";

    document.getElementById("mySidenav").style.transition = "1s";
    document.getElementById("main").style.transition = "1s";
    document.getElementById("full").style.transition = "1s";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("full").style.marginLeft = "0px";
}
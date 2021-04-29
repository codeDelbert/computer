const show = document.getElementById("showScreen")
const symbol = document.getElementById("symbol")

calc = ""

function numberClick(number) {
    if (show.value === "0") {
        show.value = number
    }else if (symbol.innerText !== ""){
        show.value = number
        symbol.innerText = ""
    }else {
        show.value += number
    }
    calc += String(number)
}

function calcClick(sym) {
    symbol.innerText = sym
    console.log(sym)
    if (sym === "+") {
        calc += "+"
    } else if (sym === "−") {
        calc += "-"
    } else if (sym === "×") {
        calc += "*" 
    } else if (sym === "÷") {
        calc += "/"
    }
}

function equals() {
    console.log(calc)
    resualt = eval(calc)
    console.log(resualt)
    show.value = resualt
    symbol.innerText = ''
}

function clearclick(){
    calc = ""
    symbol.innerText = ''
    show.value = 0
}
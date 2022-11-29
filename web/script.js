function clearAll() {
    refreshInputs()
    refreshBuffers()
}

async function getNext(element) {

    let req = await fetch("http://localhost:5000/next")
    let msg = await req.json()
    console.log(msg)

    clearAll()

    if (msg.inputs) {
        drawInputs(n_input = msg.inputs.n_source, n_query = msg.inputs.n_query)
    }
    if (msg.buffers) {
		console.log("buffer yes")
        drawBuffers(msg.buffers)
    }
    if (msg.instruments){
        drawInstruments(msg.instruments)
    }

    drawCancel(msg.cancel)

    drawTime(msg.time)

}

document.addEventListener("DOMContentLoaded", async function () {

    let req = await fetch("http://localhost:5000/init")
    let msg = await req.json()

    let input = document.getElementById("inputs")
    for (let i = 0; i < msg.n_sources; i++) {
        let newInput = document.createElement("button")
        newInput.textContent = `INPUT ${i}`
        input.appendChild(newInput);
    }

    for (let i = 0; i < msg.n_buffers; i++) {
        let where = document.getElementById("buffers")
        let newEl = document.createElement("button")
        newEl.textContent = `BUFFER ${i}`
        where.appendChild(newEl);
    }

    for (let i = 0; i < msg.n_instruments; i++) {
        let where = document.getElementById("instruments")
        let newEl = document.createElement("button")
        newEl.textContent = `INSTRUMENT ${i}`
        where.appendChild(newEl);
    }

});

function drawInstruments(newInstr) {
    let instruments = document.getElementById("instruments").children
    Array.from(instruments).forEach((instr, index) => {
        instr.textContent = newInstr[index] !== "-" ? newInstr[index] : `INSTRUMENT ${index}`
    })
}

function drawBuffers(newBufflist) {
    let buffers = document.getElementById("buffers").children
    newBufflist.forEach((buffer, index) => {
        buffers[index].textContent = buffer
    })
}

function drawInputs(n_input, n_query) {
    let inputs = document.getElementById("inputs").children
    target_input = inputs.item(n_input)
    target_input.textContent = `(${n_input}, ${n_query})`
    // target_input.style.color = 'red'
}

function refreshInputs() {
    let inputs = document.getElementById("inputs").children
    Array.from(inputs).forEach((input, index) => {
        input.textContent = `INPUT ${index}`
        // input.color = "white"
    })
}

function refreshBuffers() {
    let buffers = document.getElementById("buffers").children
    Array.from(buffers).forEach((buffer, index) => buffer.textContent = `BUFFER  ${index}`)
}

function drawCancel(cancel){
    cancelbtn = document.getElementById("cancel")
    cancelbtn.textContent = cancel !== "-" ? cancel : "CANCEL"
}

function drawTime(time_v){
    time = document.getElementById("time_value")
    time.textContent = time_v
}

async function drawTable(){
    let finish = await fetch("http://localhost:5000/finish")
    let timejson = await finish.json()

    document.getElementById("time_value").textContent = timejson["time"]

    let req = await fetch("http://localhost:5000/source_table")
    let source_table = await req.json()
    console.log(source_table)
    let table = document.getElementById("source_table")
    for (var prop in source_table){
        table.insertAdjacentHTML(position="beforeend",
            `<tr> 
                <td>${source_table[prop][0]}</td>
                <td>${source_table[prop][1]}</td>
                <td>${source_table[prop][2]}</td>
                <td>${source_table[prop][3]}</td>
                <td>${source_table[prop][4]}</td>
                <td>${source_table[prop][5]}</td>
                <td>${source_table[prop][6]}</td>
                <td>${source_table[prop][7]}</td>
             </tr>`)
    }

    req = await fetch("http://localhost:5000/instruments_table")
    let instr_table = await req.json()
    table = document.getElementById("instruments_table")
    for (var prop in instr_table){
        table.insertAdjacentHTML(position="beforeend",
            `<tr> 
                <td>${instr_table[prop][0]}</td>
                <td>${instr_table[prop][1]}</td>
             </tr>`)
    }



}
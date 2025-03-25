async function getContent() {
    const resp = await fetch("http://vm4430.kaj.pouta.csc.fi:8210")
    const data = await resp.json()
    console.log(data)
    document.querySelector("#content").innerHTML = data.message
    for (item of data.myList){
        document.querySelector("#myList").innerHTML += `<li>${item}</li>`
    }
}

async function getIp(){
    const resp = await fetch("http://vm4430.kaj.pouta.csc.fi:8211")
    const data = await resp.json()
    document.querySelector("#ip").innerHTML = data.ip

}



getContent()
getIp()
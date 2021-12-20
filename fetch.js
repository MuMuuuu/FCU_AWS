async function getQRcode(name){
    return await fetch(`/{name}/qrcode` ,{
        method: "GET",
    }).then(async res => {
        return await res.json();
    }).then(async data => {
        return (data);
    });
}


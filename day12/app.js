var page = parseInt(window.prompt("Kitabın səhifə sayı:"));

if (isNaN(page)){
    alert("Hesablamada problem baş verdi");
}
else{

    var day = parseInt(window.prompt("Neçə günə bitirməlisiniz?"));

    if (isNaN(day)){
        alert("Hesablamada problem baş verdi")
    }
    else{
        if (day != 0){
            var result = Math.floor(page / day);
    
            alert("Hər gün ən az " + result + " səhifə oxumalısınız!");
        
            console.log("Səhifə sayı: " + page);
        
            console.log("Gün sayı: " + day);
        
            console.log("Nəticə: " + result);
        }
        else{
            alert("Hesablamada problem baş verdi")
        }
    }
}



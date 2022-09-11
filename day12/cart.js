// ADD cart section

let likeBook = document.querySelector("#like_book");

let heartBook = document.querySelector("#heart_book");

// Like Book
likeBook.style.color = "blue";
likeBook.style.cursor = "pointer";
likeBook.addEventListener("click", ()=>{
    if (likeBook.style.color == "blue"){
        likeBook.style.color = "grey"; 
        likeBook.style.transform = "rotate(180deg)"
    }
    else{
        likeBook.style.color = "blue"; 
        likeBook.style.transform = "rotate(360deg)"

    }
});




// Heart Book
heartBook.style.color = "grey";
heartBook.style.cursor = "pointer";
heartBook.addEventListener("click", ()=>{
    if (heartBook.style.color == "grey"){
        heartBook.style.color = "red"; 
        setTimeout(() => {
            setTimeout(alert("Kitabı bəyəndiniz!"), 100);
        }, 1200);
    }
    else{
        heartBook.style.color = "grey"; 
        setTimeout(() => {
            setTimeout(alert("Bəyənməkdən imtina etdiniz!"), 100);
        }, 1200)
    }
});


// Cart Section
let addCart = document.querySelector("#addCart");
let countBook = document.querySelector("#countBook");
let dropdownMenu = document.querySelector(".dropdown-menu");
let sumBook = document.querySelector("#sumBook");
let listCount = document.querySelector("#listCount");

addCart.addEventListener("click", ()=>{
    if (addCart.innerText == "Səbətə əlavə et"){
        addCart.style.backgroundColor = "grey";
        addCart.innerText = 'Səbətdən çıxart';
        countBook.innerText = '1';
        let newItem = document.createElement("li");
        newItem.setAttribute("class", "dropdown-item d-flex justify-content-between container");
        newItem.innerHTML = '<p><i class="fa-solid fa-xmark text-danger"></i> Inkoqnito</p><p>12AZN</p>'
        dropdownMenu.insertBefore(newItem, dropdownMenu.children[0]);
        sumBook.innerText = "49AZN";
        listCount.innerText = "3";
    }
    else{
        addCart.innerText = "Səbətə əlavə et";
        addCart.style.backgroundColor = "blue";
        countBook.innerText = '2';
        sumBook.innerText = "37AZN";
        dropdownMenu.removeChild(dropdownMenu.firstElementChild);
        listCount.innerText = "2";
    }
})
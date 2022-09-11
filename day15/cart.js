// Variables
let addCart = document.querySelector("#addCart");
let countBook = document.querySelector("#countBook");
let dropdownMenu = document.querySelector(".dropdownMenu");
let sumBook = document.querySelector("#sumBook");
let listCount = document.querySelector("#listCount");
let alertText = document.querySelector("#alertText");
let deleteBook; 
let newItem;
let priceBook = 0;
let likeBook = document.querySelector("#like_book");
let heartBook = document.querySelector("#heart_book");

let objBooks = [
    {
        name: ' Səfillər',
        price: 21, 
    },
    {
        name: ' 1984',
        price: 16,
    },
    {
        name: ' Inkoqnito',
        price: 12,
    },
];


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


addBooks();
deleteBook = document.querySelectorAll("#deleteBook"); 


addCart.addEventListener("click", changeCount);

function changeCount(){
    if (addCart.innerText == "Səbətə əlavə et"){
        addCart.style.backgroundColor = "grey";
        addCart.innerText = 'Səbətdən çıxart';
        countBook.innerText --;
        newItem = document.createElement("li");
        newItem.setAttribute("class", "dropdown-item d-flex justify-content-between container");
        newItem.innerHTML = '<p><i class="fa-solid fa-xmark text-danger" id="deleteBook"></i> Inkoqnito</p><p><span id="bookPrice">12</span>AZN</p>'
        dropdownMenu.insertBefore(newItem, dropdownMenu.children[0]);
        alertText.innerText = "Məhsul səbətə əlavə edildi"
        listCount.innerText = dropdownMenu.childElementCount;
        deleteBook = document.querySelectorAll("#deleteBook");
        deleteBook.forEach(deleteBookFunction);
        if (listCount.innerHTML > 0){
            listCount.style.visiblity = 'visible';
            listCount.style.opacity = 1;
        }
        sumBook.innerText = parseInt(sumBook.innerText) + 12;
    }
    else{
        removeBook();
    }
}

deleteBook.forEach(deleteBookFunction)



//--------------------- Functions ---------------------------

// Initial books
function addBooks(){
    for (let i = 0; i < 2; i ++){
        for (let obj in objBooks[i]){
            if (obj == 'name'){
                dropdownMenu.children[i].firstElementChild.innerHTML = `<i class="fa-solid fa-xmark text-danger" id="deleteBook"></i> ${objBooks[i][obj]}`;
            }else{
                dropdownMenu.children[i].lastElementChild.innerText = objBooks[i][obj] + 'AZN';
                priceBook += objBooks[i][obj];
            }
        }
        sumBook.innerText = priceBook;
    }        
}


// Delete books
function deleteBookFunction(bookItem){
    bookItem.style.cursor = 'pointer';
    bookItem.addEventListener('click', ()=>{
        if (bookItem.parentElement.innerHTML == `<i class="fa-solid fa-xmark text-danger" id="deleteBook" style="cursor: pointer;"></i> Inkoqnito`){
            removeBook();
        }
        dropdownMenu.removeChild(bookItem.parentElement.parentElement)
        let deletedPrice = bookItem.parentElement.parentElement.lastElementChild.innerText;
        deletedPrice = parseInt(deletedPrice.substr(0,2));
        sumBook.innerText -= deletedPrice;
        listCount.innerText = dropdownMenu.childElementCount;
        if (listCount.innerHTML == 0){
            listCount.style.visiblity = 'hidden';
            listCount.style.opacity = 0;
        }

    });
} 


// Eject book
function removeBook(){
    addCart.innerText = "Səbətə əlavə et";
    addCart.style.backgroundColor = "blue";
    countBook.innerText ++;
    dropdownMenu.removeChild(dropdownMenu.firstElementChild);
    listCount.innerText = dropdownMenu.childElementCount;
    alertText.innerText = "Məhsul səbətdən çıxarıldı";
    if (sumBook.innerText != 0){
        sumBook.innerText = parseInt(sumBook.innerText) - 12;
    }
    if (listCount.innerHTML == 0){
        listCount.style.visiblity = 'hidden';
        listCount.style.opacity = 0;
    }
}



// day 15 -- Jquery Plugin
$(document).ready(function(){
    $('.footer-slider').slick({
        dots: false,
        arrows: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true,
        centerMode: true,
        slidesToShow: 3,
        // prevArrow:"<button type='button' class='slick-prev pull-left'><i class='fa fa-angle-left' aria-hidden='true'></i></button>",
        // nextArrow:"<button type='button' class='slick-next pull-right'><i class='fa fa-angle-right' aria-hidden='true'></i></button>"
    })
})
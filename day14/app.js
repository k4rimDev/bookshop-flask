let objBooks = [
    {
        imageSrc: '../assets/images/sefiller-book.jpeg',
        name: ' Səfillər',
        author: 'Viktor Hugo',
        price: 21, 
    },
    {   
        imageSrc: '../assets/images/1984-book.jpg',
        author: 'George Orwell',
        name: ' 1984',
        price: 16,
    },
    {   
        imageSrc: '../assets/images/inkonito-book.jpg',
        name: ' Inkoqnito',
        author: 'David Eagleman',
        price: 12,
    },
];


// Books section
$( document ).ready(function() {
    let bookIncrement = $('#bookIncrement');
    let bookDecrement = $('#bookDecrement');
    let bookStatus = $('#bookStatus');
    let parentBook = $('#parentBook');
    let count = 0;
    let bookName;
    let authorName;
    let imageLocation;
    let arrIdentical = [];


    bookIncrement.click(function(){
        
        let isIdentical = true;
        
        while(isIdentical){
            let randomBookIndex = Math.round(Math.random() * 2);

            if (arrIdentical.indexOf(randomBookIndex) < 0){
                count ++;
                bookStatus.attr('value', count)
                arrIdentical.push(randomBookIndex);
                for(let i in objBooks[randomBookIndex]){
                    if (i == 'imageSrc'){
                        imageLocation = objBooks[randomBookIndex][i]
                    }
        
                    if (i == 'name'){
                        bookName = objBooks[randomBookIndex][i]
                    }
        
                    if (i == 'author'){
                        authorName = objBooks[randomBookIndex][i]
                    }
                }
                parentBook.append(`
                <div class="col-12 mb-5 col-md-6 col-lg-4 px-5">
                    <div class="card w-100">
                        <img src=${imageLocation} class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">${bookName}</h5>
                            <p class="card-text">${authorName}</p>
                            <a href="./product.html" class="btn btn-primary">Ətraflı</a>
                        </div>
                    </div>
                </div>
            `);
            break;
            
            }
            if(arrIdentical.length == 3){
                arrIdentical = [];
            }
        }
        
    })

    bookDecrement.click(function(){
        if (count > 0){
            count --;
            parentBook.children().last().remove();
            arrIdentical.pop();
            console.log(arrIdentical);
        }
        bookStatus.attr('value', count)
    })




    // Jumbotron Section
    let searchBookPage = $('#searchBookPage');
    let calculateBtn = $('#calculateBtn');
    let alertBookPerPage = $('#alertBookPerPage');
    let pagePerDay = $('#pagePerDay');
    let alertError = $('#alertError');


    $(".book__calculator").hide();
    alertBookPerPage.hide();
    alertError.hide();

    searchBookPage.click(function(){
        $(".book__calculator").toggle();
        if ($(this).hasClass('bg-warning')){
            $(this).removeClass('bg-warning');
            $(this).addClass('bg-danger');
            $(this).css('color', 'white');
            $(this).text('Bağla')
        }else{
            $(this).removeClass('bg-danger');
            $(this).addClass('bg-warning');
            $(this).css('color', 'black');
            $(this).text('Araştır');
        }
    });

    calculateBtn.click(function(){
        let bookCount = $('#bookCount');
        let dayCount = $('#dayCount');
        if((isNaN((dayCount.val())) || isNaN((bookCount.val()))) || ((dayCount.val() == 0) || (bookCount.val() == 0))){
            alertBookPerPage.hide();
            alertError.show();

        }else{
            let answer = Math.ceil(parseInt($(bookCount).val(), 10) / parseInt($(dayCount).val(), 10));
            pagePerDay.text(answer);
            alertError.hide();
            alertBookPerPage.show();
        }            
    });
});







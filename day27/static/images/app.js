let objBooks = [
    {
        imageSrc: '../static/images/sefiller-book.jpeg',
        dataCategory: "roman",
        name: ' Səfillər',
        author: 'Viktor Hugo',
        price: 21, 
    },
    {   
        imageSrc: '../static/images/1984-book.jpg',
        dataCategory: "science",
        author: 'George Orwell',
        name: ' 1984',
        price: 16,
    },
    {   
        imageSrc: '../static/images/inkonito-book.jpg',
        dataCategory: "psychology",
        name: ' Inkoqnito',
        author: 'David Eagleman',
        price: 12,
    },
    {   
        imageSrc: '../static/images/menimadimqirmizi-book.jpeg',
        dataCategory: "roman",
        name: ' Menim adim qirmizi',
        author: 'Orhan Pamuk',
        price: 120,
    },
    {   
        imageSrc: '../static/images/xeyanet-book.jpeg',
        dataCategory: "roman",
        name: ' Xeyanet',
        author: 'Elxan Elatli',
        price: 54,
    },
    {   
        imageSrc: '../static/images/yeryuzu-book.jpeg',
        dataCategory: "science",
        name: ' Yeryuzu Muzesi',
        author: 'Hamdi Akçay',
        price: 42,
    },
    {   
        imageSrc: '../static/images/emosianal-book.jpeg',
        dataCategory: "psychology",
        name: ' Emosianal',
        author: 'Daniel Goleman',
        price: 39,
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
    let filterButtons = $('#filters button');             



    bookIncrement.click(function(){
        
        let isIdentical = true;
        
        while(isIdentical){
            let randomBookIndex = Math.round(Math.random() * 6);

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
                    if (i == 'dataCategory'){
                        dataCategory = objBooks[randomBookIndex][i]
                    }
                }
                parentBook.append(`
                <div class="col-12 mb-5 col-md-6 col-lg-4 px-5 element-item" data-category=${dataCategory}>
                    <div class="card w-100">
                        <img src=${imageLocation} class="card-img-top" alt="..." height="400">
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
            if(arrIdentical.length == 7){
                break;
            }
        }   
        

        // Filtering books
        filterButtons.click(function(){
            if ($(this).attr('data-filter') == '*'){
                parentBook.children().css('display', 'block')
            }
            if($(this).attr('data-filter') == 'psychology'){
                parentBook.children().css('display', 'none')
                parentBook.children().each(function(){
                    if ($(this).attr('data-category') == 'psychology'){
                        $(this).css('display', 'block')
                    }
                })
            }
            if($(this).attr('data-filter') == 'roman'){
                parentBook.children().css('display', 'none')
                parentBook.children().each(function(){
                    if ($(this).attr('data-category') == 'roman'){
                        $(this).css('display', 'block')
                    }
                })
            }
            if($(this).attr('data-filter') == 'science'){
                parentBook.children().css('display', 'none')
                parentBook.children().each(function(){
                    if ($(this).attr('data-category') == 'science'){
                        $(this).css('display', 'block')
                    }
                })
            }
        })
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







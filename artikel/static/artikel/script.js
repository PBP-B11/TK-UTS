
$(document).ready(function() {

getData();

$(document).on('submit',"#add-article-form",function (e) {
    e.preventDefault();

    var title  = $("#title").val();
    var url    = $("#url").val();
    var gambar = $("#gambar").val();

    $.ajax({
        type: "POST",
        url: "/article/add-article/",
        data: {
            title: title,
            url: url,
            gambar: gambar,
            csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            $("#add-article").modal('hide');
            document.getElementById("add-article-form").reset();

            $("#myarticle").empty();
            $("#card-container").empty();
            $("#carousel-content").empty();
            getData();

        },
        error: function (error) {
            console.log(error);
        },

    });

  });
  
});

function getData(){
    getCarouselArticle();
    getCardArticle();
    getMyArticle();
}

function getCarouselArticle(){
    var active = "";
    $.get("/article/artikel-populer-json/", function(data) {
        // console.log(data);
        $.each(data, function(index, artikel) {
            if (index == 0){ active = "active"; }
            $("#carousel-content").append(
                '<a href="' + artikel.fields.url + '" target="_blank">' +
                    '<div class="carousel-item ' + active + '">' +
                        '<div class="carousel-img">' +
                            '<img src="' + artikel.fields.gambar + '"class="d-block w-100">' +
                        '</div>' +
                        '<div class="carousel-caption">' +
                            '<h1>' + artikel.fields.title + '</h5>' +
                        '</div>' +
                    '</div>' +
'                </a>'
            );
            active = "";
                
        });
    });
}

function getCardArticle(){
    var technician = $("#technician").val();
    var tombol = "";

    $.get("/article/artikel-json/", function(data) {
        console.log(data);
        
        $.each(data, function(index, artikel) {
            if(technician == "True"){
                tombol = '<div class="delete mb-2" >' +
                            '<a onclick="deleteArtikel(' + artikel.pk + ')" class="btn btn-danger">Delete</a>' +
                        '</div>';
            }else{
                tombol = '<div class="like mb-2" >' +
                            '<a onclick="like(' + artikel.pk + ')" class="btn btn-primary like'+ artikel.pk + '">Like</a>' +
                        '</div>';

            }
            $("#card-container").append(
                '<div class="thumbnail">' +
                    '<a href="' + artikel.fields.url + '" target="_blank">' +
                        '<div class="card">' +
                            '<img  src="' + artikel.fields.gambar + '" alt="Card image cap">' +
                            '<div class="card-body">' +
                            '<h5 class="card-title">' + artikel.fields.title + '</h5>' +
                            '</div>' +
                        '</div>' +
                        tombol +
                    '</a>' +
                '</div>'
            );
                
        });
    });
}

function getMyArticle(){
    var styleStatusJudul ="";
    var status="";
    var technician = $("#technician").val();
    var dataAddress = "";

    if(technician == "True"){
        dataAddress = "/article/artikel-submitted-json/";
    }else{
        dataAddress = "/article/artikel-user-json/";
    }


    $.get(dataAddress, function(data) {
        console.log(data);
        $.each(data, function(index, artikel) {

            if(technician == "True"){
                status = '<a style="color: red;" onclick="deleteArtikel(' + artikel.pk + ')">Delete</a>' + 
                '<a style=" color: green;" onclick="approveArtikel(' + artikel.pk + ')">Approve</a>';
            }else if(artikel.fields.status == true){ 
                status = '<p style="color: green;">Approved</p>';
                styleStatusJudul = 'style="color: black;"'; 
            }else{
                status = '<p>Submitted</p>';
                styleStatusJudul = ''; 
            }
            $("#myarticle").append(
                '<div class="myarticle-thumbnail">'+
                    '<a href="' + artikel.fields.url + '" target="_blank">' +
                        '<div class="card myarticleCard">' +
                            '<img class="myarticleImg" src="' + artikel.fields.gambar + '" alt="Card image cap">' +

                            '<div class="card-body">'+
                                '<div><h5' + styleStatusJudul + 'class="card-title myarticle-title">' + artikel.fields.title + '</h5></div>'+
                                '<div class="status">' + status + '</div>' +
                            '</div>' +
                        '</div>' +
                    '</a>' +
                '</div>'
            );
                
        });

    });
}


function deleteArtikel(id) {
    $.ajax({
        type: "POST",
        url:"delete-article/" + id,
        data: {csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val(),},
        success: function (response) {
            $("#myarticle").empty();
            $("#card-container").empty();
            $("#carousel-content").empty();
            getData();
        },
    });
}

function approveArtikel(id) {
    $.ajax({
        type: "POST",
        url:"approve-article/" + id,
        data: {csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val(),},
        success: function (response) {
            $("#myarticle").empty();
            $("#card-container").empty();
            $("#carousel-content").empty();
            getData();
        },
    });
}

function like(id) {

    var button = ".like" + id;
    $.ajax({
        type: "POST",
        url:"add-like/" + id,
        data: {csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val() },
        success: function (response) {
                $(button).css("pointer-events","none");
                $(button).removeClass("btn-primary");
                $(button).addClass("btn-secondary");
                
        },
    });
}
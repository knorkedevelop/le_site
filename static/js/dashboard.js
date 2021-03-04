$(document).ready(function () {

    $.ajax({
        url: "/dashboard/get_cards",
        type: "get",
        success: function (response) {
            get_cards(response)
        },
        error: function (xhr) {
            //Do Something to handle error
        }
    });
});

function get_cards(myCards) {
    var html_create_card = '';
    var html_create_modal = '';
    for (let i = 0; i < myCards.cards.length; i++) {
        html_create_card += '<div class="col-md-6 col-lg-4 mb-5" draggable="true"> <div class="portfolio-item mx-auto"> <img class="img-fluid" src="' + myCards.cards[i].image + '" alt="" /> <a href="' + myCards.cards[i].url + '"><div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100"><div class="portfolio-item-caption-content text-center text-white"> <p class="inputName">' + myCards.cards[i].name + '</p></div></div></a> </div>    <div class="icon-bar"><i class="fas fa-edit  icon-left" data-toggle="modal"data-target="#portfolioModalUpdate' + myCards.cards[i].id + '"> </i> <i class="fas fa-chevron-left"onclick="move\(' + myCards.cards[i].id + ',true\)"></i><i class="fas fa-chevron-right"onclick="move\(' + myCards.cards[i].id + ',false\)"></i><i class="fas fa-trash  icon-right"onclick="delete_card\(' + myCards.cards[i].id + '\)"> </i></div></div>'
        html_create_modal += '<div class="modal fade" id="portfolioModalUpdate' + myCards.cards[i].id + '" tabindex="-1" role="dialog"aria-labelledby="portfolioModal1Label" aria-hidden="true"><div class="modal-dialog" role="document"><div class="modal-content align-items-center text-center"><table class="table table-bordered table-dark align-items-center text-center"><tr><td><button class="close" type="button" data-dismiss="modal" aria-label="Close"><span aria-hidden="true"><i class="fas fa-times"></i></span></button><div class="divider-custom"><div class="divider-custom-line"></div> <h2 class="portfolio-modal-title text-uppercase" id="portfolioModal1Label"> Update card</h2><div class="divider-custom-line"></div></div> </td></tr><tr> <td> <h3>Name</h3> <input type="text" class="form-control" id="inputName' + myCards.cards[i].id + '"placeholder="Mein Name" value="' + myCards.cards[i].name + '"> </td></tr><tr><td> <h3>Link </h3><input type="text" class="form-control" id="inputURL' + myCards.cards[i].id + '"placeholder="Mein Link" value="' + myCards.cards[i].url + '"></td> </tr> <tr> <td> <h3>Bild [.png]</h3><input type="file" class="form-control" id="inputImage' + myCards.cards[i].id + '"placeholder="Mein Bild"></td> </tr><tr> <td><button class=" btn btn-primary" data-dismiss="modal" onclick="update_card1\(' + myCards.cards[i].id + '\)"> <i class="fas fa-times fa-fw"></i>Update Card </button></td> </tr> </table></div></div></div>'
    }
    document.getElementById("myCards").innerHTML = html_create_card + document.getElementById("myCards").innerHTML
    document.body.innerHTML += html_create_modal
    return
}

//create_card
function create_card() {
    var image = document.getElementById("inputImage").files[0]
    var url = $('#inputURL').val();
    var name = $('#inputName').val();
    var reader = new FileReader();
    reader.readAsDataURL(image);
    reader.onload = function () {
        image = reader.result
        $.ajax({
            url: "/dashboard/create_card",
            type: "get",
            data: { url: url, image: image, name: name },
            success: function () {
                location.reload();
            }
        });
    };

}

// delete_card
function delete_card(myID) {

    var id = myID
    $.ajax({
        url: "/dashboard/delete_card",
        type: "get",
        data: { id: id },
        success: function () {
            location.reload();
        }

    });
}


// update_card
function update_card1(myID) {
    var image = document.getElementById("inputImage" + myID).files[0]
    var url = $('#inputURL' + myID).val();
    var name = $('#inputName' + myID).val();
    var reader = new FileReader();
    var id = myID
    if (image != null) {
        reader.readAsDataURL(image);
        reader.onload = function () {
            image = reader.result
            update_card2(id, url, image, name)
        }
    } else {
        image = ""
        update_card2(id, url, image, name)
    }
}



function update_card2(id, url, image, name) {
    $.ajax({
        url: "/dashboard/update_card",
        type: "get",
        data: { id: id, url: url, image: image, name: name },
        success: function (response) {
            (response)
            location.reload();
        }
    });
}

// move
function swap_cards(myID, left) {
    if (left) {
        direction = "left"
    } else {
        direction = "right"
    }
    var id = myID
    $.ajax({
        url: "/dashboard/swap_cards",
        type: "get",
        data: { id: id, direction: direction },
        success: function () {
            location.reload();
        }
    });
}
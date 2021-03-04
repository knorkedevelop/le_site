function getUsers() {
    $.ajax({
        url: "/admin/get_users",
        type: "get",
        success: function (response) {
            users = response.users
            config_table = ''
            for (current_user of users) {
                config_table += '<tr><td><input type="text" class="form-control" value=' + current_user.id + ' id="adminID' + current_user.id + '"></td><td><input type="text" class="form-control" value="' + current_user.name + '" id="adminName' + current_user.id + '"></td><td><input type="text" class="form-control" placeholder="Neues Passwort" id="adminPassword' + current_user.id + '"><input type="text" class="form-control" placeholder="Passwort wiederholen" id="adminPasswordSecond' + current_user.id + '"></td><td><i class="fas fa-check-square config_icons" onclick="update_profile1\(' + current_user.id + ', true\)"></i><i class="fas fa-trash config_icons" onclick="delete_user\(' + current_user.id + '\)"></i></td> </tr>'
            }
            document.getElementById("user_config_table").innerHTML = config_table
        },

    });
}

function create_user(id) {
    var name = $('#new_user_name').val()
    var password = $('#new_user_password').val()
    var password_second = $('#new_user_password_second').val()
    if (password == password_second) {
        $.ajax({

            url: "/admin/create_user",
            type: "get",
            data: { id: id, name: name, password: password },
            success: function () {
                location.reload();
            }


        });
    }
}


function delete_user(id) {
    $.ajax({
        url: "/admin/delete_user",
        type: "get",
        data: { id: id },
        success: function () {
            location.reload();
        }

    });
}


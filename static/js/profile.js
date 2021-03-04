
$(document).ready(function () {
  get_profile(false)
});


function get_profile(for_profile) {
  $.ajax({
    url: "/profile/get_profile",
    type: "get",
    success: function (response) {
      if (for_profile) {
        $("#profilePreview").attr("src", response["user"].image)
        $("#profileName").attr("value", response["user"].name)
      } else {
        $("#user_image").attr("src", response["user"].image)
        $("#user_name").text(response["user"].name)
        if (response["user"].id == "1") {
          document.getElementById("user_config").style.visibility = "visible"
        } else {
          document.getElementById("user_config").style.visibility = "hidden"
        }
      }
    },
    error: function (xhr) {
      ("Error")
    }
  });
}

function logout() {
  $.ajax({
    url: "/profile/logout",
    type: "get",
  });
}
function update_profile1(id = -1, asAdmin = false) {
  username = ""
  image = null
  password = ""
  passwordSecond = ""
    (id)
  if (asAdmin) {
    username = $('#adminName' + id).val();
    password = $('#adminPassword' + id).val();
    passwordSecond = $('#adminPasswordSecond' + id).val();
  } else {
    (id)
    username = $('#profileName').val();
    image = document.getElementById("profileImage").files[0]
    password = $('#profilePassword').val();
    passwordSecond = $('#profileSecondPassword').val();
  }
  var reader = new FileReader();
  if (password == passwordSecond) {
    if (image != null) {
      reader.readAsDataURL(image);
      reader.onload = function () {
        image = reader.result
        update_profile2(id, username, image, password)
      };
    } else {
      update_profile2(id, username, image, password)
    }

  }
}

function update_profile2(id, name, image, password) {
  $.ajax({
    url: "/profile/update_profile",
    type: "get",
    data: { id: id, name: name, image: image, password: password },
    success: function () {
      location.reload();
    }
  });
}











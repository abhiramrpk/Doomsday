$(document).ready(function () {

    // window.onload = check()

    let script;
    var index = parseInt(document.getElementById('val').value);

    document.getElementById('bt3').addEventListener("click", chat);
    // document.getElementById('i1').addEventListener("click", imglb);
    document.getElementById('i2').addEventListener("click", formvie);
    function formvie()
    {var clue2fom= document.getElementById("clueform2");
        clue2fom.style.visibility = "visible";
    }
    function chat() {
        $("#r-chat").hide();
        $("#l-chat").hide();
        lb();
    }



    function lb() {
        setTimeout(
            function open(event) {

                document.querySelector(".popup").style.display = "block"
            },
        )
    };



    document.querySelector("#close").addEventListener("click", function () {
        document.querySelector(".popup").style.display = "none";
    });

    // function imglb() {
    //     setTimeout(
    //         function open(event) {

    //             document.querySelector(".imgpopup").style.display = "block"
    //         },
    //     )
    // };



    // document.querySelector("#close").addEventListener("click", function () {
    //     document.querySelector(".imgpopup").style.display = "none";
    // });



    readFile();
    function readFile() {
        fetch('../static/script.txt')
            .then(response => response.text())
            .then(data => fun(data))
            .catch(error => console.error(error))

    }


    function fun(data) {

        script = data.split("\n").map(line => {
            let parts = line.split(":");
            let left = parts[0];
            let right = parts[1];
            let dialogue = parts[2];
            return { left, right, dialogue };
        });

    }


    var l_img = document.getElementById('left-img');
    var r_img = document.getElementById('right-img');
    var flag = 0;





    function next() {

        $("#r-chat").hide();
        $("#l-chat").hide();
        l_img.style.visibility = "hidden";
        r_img.style.visibility = "hidden";


        



        if (script[index].dialogue != undefined) {

            if (script[index].right.includes(".png")) {
                r_img.style.visibility = "visible";
            }
            if (script[index].left.includes(".png")) {
                l_img.style.visibility = "visible";
            }


            function printLetterByLetter(did, text) {
                var ind = 0;
                var textContainer = document.getElementById(did);

                function addLetter() {
                    if (ind < text.length) {
                        textContainer.innerHTML += text.charAt(ind);
                        ind++;
                        setTimeout(addLetter, 20);
                    }
                }
                addLetter();
                textContainer.innerHTML = ''

            }


            if (index % 2 == 0) {


                l_img.src = "../static/images/characters/" + script[index].left.replace(" ", "");
                r_img.src = "../static/images/characters/" + script[index].right.replace(" ", "");

                printLetterByLetter('l-chat', script[index].dialogue);


                $("#l-chat").show();


                flag = 1;
            }
            else {
                r_img.src = "../static/images/characters/" + script[index].right.replace(" ", "");
                l_img.src = "../static/images/characters/" + script[index].left.replace(" ", "");


                printLetterByLetter('r-chat', script[index].dialogue);

                $("#r-chat").show();

                flag = 0;
            }
        }
        else if (script[index].left.includes('.jpg')) {
            document.body.style.backgroundImage = "url('../static/images/background/" + script[index].left.replace('\r', '') + "')";


        }
        else if (script[index].left == "#") {
        index+=1;
        next();
        }


    };

    document.getElementById('bt').addEventListener("click", check)

    function check() {

        console.log(script[index]);
        console.log(index);
        if (index == '21'||index == '29'||index == '47'||index == '62'||index == '83'||index == '86'||index == '99') {

            document.getElementById('myform').submit();
        }
        else {

            next();

            document.getElementById('ind').value = index;


        }
        
        index += 1;
    }

    function previous() {

        if (index >= 1) {
            index -= 1;
            if (script[index].left == '#') {
                index = index - 1;
                previous();
            }
            else {




                $("#r-chat").hide();
                $("#l-chat").hide();
                l_img.style.visibility = "hidden";
                r_img.style.visibility = "hidden";

                if (script[index].dialogue != undefined) {

                    if (script[index].right.includes(".png")) {
                        r_img.style.visibility = "visible";
                    }
                    if (script[index].left.includes(".png")) {
                        l_img.style.visibility = "visible";
                    }

                    function printLetterByLetter(did, text) {
                        var ind = 0;
                        var textContainer = document.getElementById(did);


                        function addLetter() {
                            if (ind < text.length) {
                                textContainer.innerHTML += text.charAt(ind);
                                ind++;
                                setTimeout(addLetter, 20);
                            }
                        }
                        addLetter();
                        textContainer.innerHTML = ''


                    }


                    if (index % 2 == 0) {
                        r_img.src = "../static/images/characters/" + script[index].right.replace(" ", "");
                        l_img.src = "../static/images/characters/" + script[index].left.replace(" ", "");


                        printLetterByLetter('l-chat', script[index].dialogue);


                        $("#l-chat").show();


                        flag = 1;
                    }
                    else {
                        l_img.src = "../static/images/characters/" + script[index].left.replace(" ", "");
                        r_img.src = "../static/images/characters/" + script[index].right.replace(" ", "");


                        printLetterByLetter('r-chat', script[index].dialogue);

                        $("#r-chat").show();

                        flag = 0;
                    }
                }
                else {
                    // document.getElementById('b').background;
                    if (script[index].left.includes('.jpg')) {
                        document.body.style.backgroundImage = "url('../static/images/background/" + script[index].left.replace('\r', '') + "')";
                        index -= 1;
                    }


                }

            }
        }
    };
    document.getElementById('bt2').addEventListener("click", previous)
});



  //Получим форму поиска и ссылки на страницы
  let search = document.getElementById("search");
  let pageLinks = document.getElementsByClassName("page-link");

  //Убедимся, что форма поиска существует
  if (search) {
    for (let i = 0; pageLinks.length > i; i++) {
      pageLinks[i].addEventListener('click', function (e) {
        e.preventDefault();

        let page = this.dataset.page

        search.innerHTML += `<input value=${page} name="page" hidden`
        search.submit()
      })
    }
  }



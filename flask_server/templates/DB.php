<!DOCTYPE html>

<html lang="ru">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css">
    <script src="/js/main.js"></script>
    <title>База данных</title>
</head>


<!--PHP SCRIPT -->
<?php
$user = 'root';
$pass = '';
$db_name = 'WEB';
$hostname = 'localhost';

/* создать соединение */ 
$db = new mysqli($hostname, $user, $pass, $db_name) OR DIE("Не могу создать соединение ");
$result = mysqli_query($db, 
'SELECT * from author a 
join news n on n.author_id = a.id');
?>

<style>
   .general{
      background: #FF8926;
   }
   <?php include 'css/main.css';?>
</style>
<body>

<!--HEADER-->
   <header class="db_header">
      <nav class="navbar navbar-expand bg-dark">
         <ul class="navbar-nav d-flex align-items-center">
            <li>
               <a href="index.html" class="navbar-brand">
                  <img src="img/logo.png" alt="logo" class="header__logo">
               </a>
            </li>
            <li class="navbar__item">
               <a class="nav-link" href="index.html">Главная страница</a>
            </li>
            <li class="navbar__item">
               <a class="nav-link" href="second.html">Вторая страница</a>
            </li>
            <li class="navbar__item">
               <a class="nav-link" href="links.html">Источники</a>
            </li>
            <li class="navbar__item">
               <a class="nav-link" href="js.html">JS</a>
            </li>
            <li class="navbar__item">
               <a class="nav-link" href="form.html">Форма</a>
            </li>
            <li class="navbar__item">
               <a class="nav-link" href="DB.php">База данных</a>
            </li>
            <li class="navbar__item">
               <a class="nav-link" href="xml.html">XML</a>
            </li>
         </ul>
      </nav>
         <div class="container">
               <div class="header__content mt-5 d-flex flex-column align-items-center">
                  <h1>База данных</h1>
                  <h5>Лабораторная работа №6</h5>
               </div>
         </div>
   </header>

<!--FIRST SECTION-->
   <section class="general pt-5 pb-5">
      <div class="container">
         <h2 class='text-center mb-5'>Новости</h2>

         <?php foreach($result as $record): ?>
   
            <h4 class='text-center mt-5'> <?=$record['title']?> </h4>
            <div class="history__article d-flex">
               <div class="article article__second">
                  <p class="article__text">
                     <?=$record['post_text']  ?>
                     <h6> <?=$record['surname'] . ' '. $record['name'] . ' ' 
                     . $record['patronym'] . ', ' . $record['position'] ?> </h6>
                     <h6><?=$record['post_date'] ?></h6> 
                  </p>
               </div>
               <img src="img/<?=$record['img_path']?>" alt="Komp" class="history__img komp db_img"> 
         </div>

         <?php endforeach; ?>

      </div>
   </section>


<!--FOOTER-->
   <footer class="bg-info text-black">
        <div class="container">
            <ul class="list-gtoup footer__list d-block">
               <li class="list-group-item">
                  <p>
                     Тропин Иван, гр.4933
                  </p>
               </li>
               <li class="list-group-item">
                  <a href="#" class="footer__link">
                     <i class="bi bi-instagram"> Instagram</i>
                  </a>
               </li>
               <li class="list-group-item">
                  <a href="#">
                     <i class="bi bi-github"> Github</i>
                  </a>
               </li>
               <li class="list-group-item">
                  <a href="#">
                     <i class="bi bi-telegram"> Telegram</i>
                  </a>
               </li>
            </ul>
        </div>
   </footer>
</body>
</html>







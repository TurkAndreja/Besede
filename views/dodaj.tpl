% rebase("osnova.tpl")


<section class="hero">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">
        Besede in življenje
      </h1>
    </div>
  </div>
</section>

<section>
  <div class="container is-fluid">
    <div class="notification">
      V skladu s slovničnimi pravili dodaj podatke o besedilu! 
    </div>
  </div>
</section>

<section>
  <form action="/dodano/" method="post">
    <div class="columns">
      <div class="column is-one-quarter">
        <br><input name = "avtor" class="input" type="text" placeholder="avtor"></br>
        <br><input name = "tema" class="input" type="text" placeholder="tema"></br>
        <br><input name = "kljucne_besede" class="input" type="text" placeholder="ključne besede"></br>
        <br></br>
      </div>
    <div class="column is-two-quarters">
      <br><textarea name = "besedilo" class="textarea" placeholder="besedilo"></textarea></br>
    </div>
    <div class="column is-one-quarter"
    </div>
 </div>
</section>


<section>
  <div class="container is-fluid">
    <div class="notification">
      Dodaj podatke o knjigi, če so poznani!
    </div>
  </div>
</section>

<section>
  <div class="columns">
    <div class="column is-one-quarter">
      <br><input name = "naslov" class="input" type="text" placeholder="naslov"></br>
      <br><input name = "stran" class="input" type="text" placeholder="stran"></br>
      <br><input name = "leto_izida" class="input" type="text" placeholder="leto izdaje"></br>
      <br><input name = "zalozba" class="input" type="text" placeholder="založba"></br>
      <br></br>
    </div>
  </div>
</section>


<section>
  <div class="container is-fluid">
    <div class="notification buttons">
       <input class="button button is-white is-small" type="submit" value="DODAJ">

  </form>

    <br></br>
      <form action="/" method="get">
        <input class="button button is-white is-small" type="submit" value="NAZAJ">
      </form>
    </div>
  </div>
</section>







    

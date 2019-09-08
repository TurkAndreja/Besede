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
      Dodaj podatke, po katerih želiš iskati besedilo!
    </div>
  </div>
</section>

<section>
  <form action="/najdeno/" method="post">
    <div class="columns">
      <div class="column is-one-third">
        <br><input name = "avtor" class="input" type="text" placeholder="avtor"></br>
        <br><input name = "tema" class="input" type="text" placeholder="tema"></br>
        <br><input name = "kljucne_besede" class="input" type="text" placeholder="ključne besede"></br>
        <br><input name = "naslov" class="input" type="text" placeholder="naslov knjige"></br>
        <br></br>
      </div>
    </div>
</section>


<section>
<div class="container is-fluid">
  <div class="notification buttons">
     <input class="button button is-white is-small" type="submit" value="POIŠČI">

</form>

     <br></br>
     <form action="/" method="get">
        <input class="button button is-white is-small" type="submit" value="NAZAJ">
     </form>
  </div>
</div>
</section>





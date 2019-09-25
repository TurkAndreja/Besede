% rebase('osnova.tpl')

<section>
    <div class="container is-fluid">
      <div class="notification">
        <p class = "subtitle"><em>"{{besedilo.besedilo}}"</em> <small>({{besedilo.avtor[0]}}
    
        %if besedilo.knjiga.naslov is not None:
            , {{!besedilo.besedilo.replace("\r\n", "<br>")})</small></p>
        %else:
            )</small></p>
        %end
        
        <form action="/" method="get">
          <input class="button button is-white is-normal" type="submit" value="KAKO LEPO, HVALA!" :)">
        </form>
      </div>
    </div>
</section>

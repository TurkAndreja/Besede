% rebase('osnova.tpl')

<div class="container notification is-white">
<form action="/" method="get">
    <input class="button button is-light is-normal is-pulled-right" type="submit" value="SEM NAŠEL / NAŠLA! :)">
</form>
</div>

% for b in seznam:  
    <div class="container notification">
        <p><em>"{{!b.besedilo.replace("\r\n", "<br>")}}"</em> <small>({{b.avtor[0]}} 
            %if b.knjiga.naslov is not None:
                , {{b.knjiga.naslov}})</small></p> 
            %elif b.knjiga.naslov is not None and b.knjiga.stran is not None:
                , {{b.knjiga.naslov}}, {{b.knjiga.stran}})</small></p>
            %else:
                )</small></p>
    % end
    </div>


 

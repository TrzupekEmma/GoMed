
import sqlite3
def add_actor(conn, actor):
    # insert table statement
    sql = ''' INSERT INTO actors(id,name,photo)
              VALUES(?,?,?) '''
    
    # Create  a cursor
    cur = conn.cursor()

    # execute the INSERT statement
    cur.execute(sql, actor)

    # commit the changes
    conn.commit()

    # get the id of the last inserted row
    return cur.lastrowid

ACTORS = [
{"id":26073614,"name":"Al Pacino","photo":"https://placebear.com/342/479"},
{"id":77394988,"name":"Anthony Hopkins","photo":"https://placebear.com/305/469"},
{"id":44646271,"name":"Audrey Hepburn","photo":"https://placebear.com/390/442"},
{"id":85626345,"name":"Barbara Stanwyck","photo":"https://placebear.com/399/411"},
{"id":57946467,"name":"Barbra Streisand","photo":"https://placebear.com/328/490"},
{"id":44333164,"name":"Ben Kingsley","photo":"https://placebear.com/399/442"},
{"id":91171557,"name":"Bette Davis","photo":"https://placebear.com/318/496"},
{"id":25163439,"name":"Brad Pitt","photo":"https://placebear.com/359/430"},
{"id":59236719,"name":"Cate Blanchett","photo":"https://placebear.com/346/407"},
{"id":35491900,"name":"Christian Bale","photo":"https://placebear.com/363/440"},
{"id":48725048,"name":"Christoph Waltz","photo":"https://placebear.com/356/445"},
{"id":36858988,"name":"Christopher Walken","photo":"https://placebear.com/328/448"},
{"id":77052052,"name":"Clint Eastwood","photo":"https://placebear.com/311/428"},
{"id":74729990,"name":"Daniel Day-Lewis","photo":"https://placebear.com/393/480"},
{"id":75495971,"name":"Denzel Washington","photo":"https://placebear.com/392/471"},
{"id":49842505,"name":"Diane Keaton","photo":"https://placebear.com/310/462"},
{"id":16533679,"name":"Dustin Hoffman","photo":"https://placebear.com/306/425"},
{"id":77778079,"name":"Ed Harris","photo":"https://placebear.com/365/430"},
{"id":62340777,"name":"Edward Norton","photo":"https://placebear.com/356/486"},
{"id":45282572,"name":"Elizabeth Taylor","photo":"https://placebear.com/338/440"},
{"id":98253023,"name":"Ellen Burstyn","photo":"https://placebear.com/313/452"},
{"id":14389118,"name":"Emma Thompson","photo":"https://placebear.com/314/445"},
{"id":85245270,"name":"Faye Dunaway","photo":"https://placebear.com/352/495"},
{"id":77497258,"name":"Frances McDormand","photo":"https://placebear.com/368/404"},
{"id":69175505,"name":"Gary Oldman","photo":"https://placebear.com/380/468"},
{"id":52103198,"name":"Gene Hackman","photo":"https://placebear.com/326/464"},
{"id":53511355,"name":"George Clooney","photo":"https://placebear.com/350/405"},
{"id":46135141,"name":"Glenn Close","photo":"https://placebear.com/318/446"},
{"id":67466115,"name":"Grace Kelly","photo":"https://placebear.com/396/422"},
{"id":32111872,"name":"Greer Garson","photo":"https://placebear.com/331/464"},
{"id":38069638,"name":"Greta Garbo","photo":"https://placebear.com/344/467"},
{"id":30546602,"name":"Harrison Ford","photo":"https://placebear.com/324/471"},
{"id":78852790,"name":"Harvey Keitel","photo":"https://placebear.com/302/498"},
{"id":75916952,"name":"Heath Ledger","photo":"https://placebear.com/354/420"},
{"id":44647231,"name":"Helen Mirren","photo":"https://placebear.com/390/401"},
{"id":98319284,"name":"Hilary Swank","photo":"https://placebear.com/334/428"},
{"id":73307095,"name":"Holly Hunter","photo":"https://placebear.com/388/439"},
{"id":65927229,"name":"Ian McKellen","photo":"https://placebear.com/359/447"},
{"id":84415199,"name":"Ingrid Bergman","photo":"https://placebear.com/341/487"},
{"id":28676619,"name":"Jack Nicholson","photo":"https://placebear.com/335/461"},
{"id":66339602,"name":"Jane Fonda","photo":"https://placebear.com/323/471"},
{"id":22447589,"name":"Jane Wyman","photo":"https://placebear.com/373/469"},
{"id":52907687,"name":"Javier Bardem","photo":"https://placebear.com/366/421"},
{"id":35506267,"name":"Jeff Bridges","photo":"https://placebear.com/388/422"},
{"id":16807306,"name":"Jennifer Jones","photo":"https://placebear.com/333/498"},
{"id":63521043,"name":"Jessica Lange","photo":"https://placebear.com/309/413"},
{"id":91132400,"name":"Joan Crawford","photo":"https://placebear.com/322/437"},
{"id":74127064,"name":"Joan Fontaine","photo":"https://placebear.com/329/458"},
{"id":30283700,"name":"Joaquin Phoenix","photo":"https://placebear.com/316/452"},
{"id":40834926,"name":"Jodie Foster","photo":"https://placebear.com/307/439"},
{"id":59676726,"name":"Joe Pesci","photo":"https://placebear.com/388/434"},
{"id":18959030,"name":"Johnny Depp","photo":"https://placebear.com/337/422"},
{"id":19220801,"name":"Judi Dench","photo":"https://placebear.com/397/480"},
{"id":41880845,"name":"Judy Garland","photo":"https://placebear.com/352/472"},
{"id":38744009,"name":"Julia Roberts","photo":"https://placebear.com/331/441"},
{"id":46032709,"name":"Julianne Moore","photo":"https://placebear.com/331/402"},
{"id":63172387,"name":"Julie Andrews","photo":"https://placebear.com/320/416"},
{"id":28367735,"name":"Kate Winslet","photo":"https://placebear.com/329/432"},
{"id":31109338,"name":"Katharine Hepburn","photo":"https://placebear.com/366/475"},
{"id":81511778,"name":"Kathy Bates","photo":"https://placebear.com/387/440"},
{"id":58030620,"name":"Kevin Spacey","photo":"https://placebear.com/321/425"},
{"id":96645151,"name":"Leonardo DiCaprio","photo":"https://placebear.com/347/495"},
{"id":57846776,"name":"Luise Rainer","photo":"https://placebear.com/311/448"},
{"id":26406570,"name":"Marilyn Monroe","photo":"https://placebear.com/305/441"},
{"id":17017025,"name":"Matt Damon","photo":"https://placebear.com/306/421"},
{"id":84422863,"name":"Mel Gibson","photo":"https://placebear.com/301/484"},
{"id":26357464,"name":"Meryl Streep","photo":"https://placebear.com/343/401"},
{"id":87469606,"name":"Michael Caine","photo":"https://placebear.com/309/481"},
{"id":50738795,"name":"Michael Douglas","photo":"https://placebear.com/393/496"},
{"id":61071401,"name":"Morgan Freeman","photo":"https://placebear.com/348/448"},
{"id":28005840,"name":"Natalie Portman","photo":"https://placebear.com/323/448"},
{"id":50786809,"name":"Natalie Wood","photo":"https://placebear.com/386/458"},
{"id":40122578,"name":"Nicolas Cage","photo":"https://placebear.com/319/481"},
{"id":75794861,"name":"Nicole Kidman","photo":"https://placebear.com/375/443"},
{"id":81504488,"name":"Olivia de Havilland","photo":"https://placebear.com/388/450"},
{"id":43406362,"name":"Paul Newman","photo":"https://placebear.com/335/456"},
{"id":44428849,"name":"Peter O'Toole","photo":"https://placebear.com/313/467"},
{"id":60338818,"name":"Philip Seymour Hoffman","photo":"https://placebear.com/389/458"},
{"id":56249953,"name":"Ralph Fiennes","photo":"https://placebear.com/301/467"},
{"id":33056256,"name":"Robert De Niro","photo":"https://placebear.com/339/439"},
{"id":36150440,"name":"Robert Downey Jr.","photo":"https://placebear.com/393/409"},
{"id":55284258,"name":"Robert Duvall","photo":"https://placebear.com/310/472"},
{"id":49032807,"name":"Robert Redford","photo":"https://placebear.com/326/443"},
{"id":14332961,"name":"Russell Crowe","photo":"https://placebear.com/336/436"},
{"id":47048008,"name":"Sally Field","photo":"https://placebear.com/301/452"},
{"id":64664156,"name":"Samuel L. Jackson","photo":"https://placebear.com/364/491"},
{"id":63841892,"name":"Sean Penn","photo":"https://placebear.com/344/496"},
{"id":80868139,"name":"Shirley MacLaine","photo":"https://placebear.com/389/475"},
{"id":22571419,"name":"Sigourney Weaver","photo":"https://placebear.com/304/464"},
{"id":23127852,"name":"Sissy Spacek","photo":"https://placebear.com/318/427"},
{"id":91913599,"name":"Sophia Loren","photo":"https://placebear.com/360/476"},
{"id":34324158,"name":"Steve Buscemi","photo":"https://placebear.com/367/467"},
{"id":54027019,"name":"Susan Hayward","photo":"https://placebear.com/376/476"},
{"id":49932101,"name":"Susan Sarandon","photo":"https://placebear.com/335/480"},
{"id":28040377,"name":"Tom Cruise","photo":"https://placebear.com/305/482"},
{"id":34061331,"name":"Tom Hanks","photo":"https://placebear.com/344/424"},
{"id":24724551,"name":"Tommy Lee Jones","photo":"https://placebear.com/315/465"},
{"id":27085641,"name":"Viola Davis","photo":"https://placebear.com/368/481"},
{"id":91326710,"name":"Vivien Leigh","photo":"https://placebear.com/388/435"},
{"id":68598976,"name":"Willem Dafoe","photo":"https://placebear.com/347/447"}
]

conn = sqlite3.connect("actors.db")
for actor in ACTORS:
	add_actor(conn,(actor["id"],actor["name"],actor["photo"]));


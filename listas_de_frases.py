desps = ["A dios, nos vemos mañana", "Descansa", "chao","Nos vemos mañana. Si dios quiere", "a dios, recuerda hidratarte", "a dios, no olvides tus medicamentos"]
song_list = ["harry_notificacion","metal_gear_pick_up","noti_benja","banana_coin_louder",
             "botw_interact_short","botw_item_discovery","bw_pokemon_catch","level_up", "midna_appears", "shiekah_slate", "zelda", "zelda_game_start", "zelda_notify"]
despedida = ["chao", "nos vemos", "Que la fuerza te acompañe", "adiós" ]
off= ["sotc_sky_burial"]
helpp=["ayuda","ayuda ayuda", "me caí",  "necesito ayuda", "me duele", "incendio", "hay fuego", "hay humo"]
buenos_dias = ["Despertar es dejar de dormir, no dejar de soñar. ¡Buenos días!" , "La vida se prepara con amor, se condimenta con fe, y se vive con agradecimiento. ¡Buenos días!",
                "Un buen día comienza con una buena actitud y una buena taza de café.", "La vida siempre te ofrece otra oportunidad y se llama 'HOY'. ¡Buenos días!",
               "¡Buenos días! Que las tristezas de la vida no nos quiten nunca la alegría de vivir.", "EL DESTINO ES ALGO EXTRAÑO, NUNCA SE SABE CÓMO VAN A RESULTAR LAS COSAS: PERO SI MANTIENES TU MENTE Y CORAZÓN ABIERTOS, TE PROMETO QUE ENCONTRARÁS TU PROPIO DESTINO ALGÚN DÍA.Que tengas un buen día",
               "ES IMPORTANTE ADQUIRIR EL CONOCIMIENTO DE DIFERENTES PENSAMIENTOS, OPINIONES Y PUNTOS DE VISTA. SI LO HACES DESDE UNO SOLO, TE VUELVES RÍGIDO Y TEDIOSO. SI ENTIENDES AL RESTO, SERÁS ALGUIEN COMPLETO. Que tengas un buen día",
               "LO MÁS IMPORTANTE ES SIEMPRE CREER EN UNO MISMO, PERO UNA PEQUEÑA AYUDA DE LOS DEMÁS ES UNA GRAN BENDICIÓN. Que tengas un excelente día", "LA PERFECCIÓN Y EL PODER ESTÁN SOBREVALORADOS. CREO QUE ES MÁS SABIO ELEGIR LA FELICIDAD Y EL AMOR. Que tengas buen día",
               "SI BUSCAS LA LUZ, A MENUDO PODRÁS ENCONTRARLA… PERO SI BUSCAS LA OSCURIDAD, ES TODO LO QUE VERÁS SIEMPRE. Que tengas buen día", "CREO QUE LAS PERSONAS PUEDEN CAMBIAR SU VIDA SI SE LO PROPONEN. CREO EN LAS SEGUNDAS OPORTUNIDADES. Buen día",
               "NUNCA DEBES RENDIRTE A LA DESESPERACIÓN. SI TE PERMITES IR POR ESE CAMINO, TE RENDIRÁS A TUS INSTINTOS MÁS BAJOS. EN TIEMPOS OSCUROS, LA ESPERANZA ES ALGO QUE TE DAS A TI MISMO. ESE ES EL SIGNIFICADO DE LA  VERDADERA FUERZA INTERIOR. Que tengas un buen día",
               "NO HAY NADA DE MALO EN DEJAR QUE QUIENES TE QUIEREN TE AYUDEN. ten un buen día", "MUCHAS COSAS QUE PARECEN AMENAZANTES EN LA OSCURIDAD, SE VUELVEN AGRADABLES CUANDO LAS ILUMINAMOS. Ten un buen día",
               "¿ES TU DESTINO O EL DESTINO AL QUE ALGUIEN MÁS QUISO OBLIGARTE? ES HORA DE QUE MIRES EN TU INTERIOR Y EMPIECES A HACERTE ESTAS DOS GRANDES PREGUNTAS: ¿QUIÉN ERES? Y ¿QUÉ ES LO QUE TÚ QUIERES? Ten un buen día",
               "TU VIDA ESTÁ DONDEQUIERA QUE ESTÉS, TE GUSTE O NO. Buen día", "EL ORGULLO NO ES LO OPUESTO DE LA VERGÜENZA SINO SU FUENTE; LA HUMILDAD PURA ES EL ÚNICO ANTÍDOTO PARA LA VERGÜENZA. Ten un buen día", "SIGUE TU PASIÓN Y LA VIDA TE PREMIARÁ. Ten un buen día",
               "A VECES LA MEJOR FORMA DE RESOLVER TUS PROBLEMAS… ES AYUDANDO A ALGUIEN MÁS. Buen día"]

lista_funciones= ["Puedo darte la fecha", "La hora", "Lo que hace la aplicacion 2","Lo que hace la aplicacion 3", "Si tienes alguna emergencia, puedo contactar a un familiar, solo tienes que pedirme ayuda", "puedo recordarte las dunciones que tengo",
                  "Y recuerda, que si necesitas algo, no tienes mas que decir mi nombre y escuchare tu orden", "Y si no me necesitas, solo debemos despedirnos y descansare hasta me necesites"]


accioness = """ Darte la hora, 
                la fecha,  
                Si necesitas ayuda, solo debes avisarme y pedire ayuda por ti,
                podemos jugar juegos de letras o matemáticas, para estimular los procesos cognitivos,
                Y si olvidas mi nombre, siempre puedes preguntar cómo me llamo
                Para que empecemos a interactuar, solo di mi nombre. Recuerda que es carla.
                """
sugerencia = """ Antes de empezar, te sugiero que tengas a mano un lapiz y un cuaderno, y cuando estes listo, solo di LISTO!"""
# ------------------------- frases orden arfabetico -----------------------



instrucciones_or_alfa = """BIENVENIDO A ORDEN ALFABÉTICO!. E juego consiste en darte un campo y luego palabras relacionadas a ese campo. 
Estas palabras, deberas ordenarlas alfabeticamente. Por ejemplo: si el campo seleccionado es el mar, las palabras pueden ser, estrella , arena y delfin, y el 
orden correcto seria arena, defil y estrella, ya que primero esta la a, de arena, luego d de delfin y luego e de estrella."""

campos = {
    'Mar':["arena", "sol","agua", "pez", "foca", "barco", "toalla"],
    'Campo': ["vaca","cerdo","caballo","conejo", "zorros","insectos"],
    'Ciudad':["auto", "metro", "semáforo", "estadio", "autopista"],
    'Animales':["mariposa", "cangrejo", "delfín", "tiburón", "tortuga", "cocodrilo", "calamar"],
    'Casa':["muebles", "horno", "dormitorio", "cocina", "silla", "sofá", "colchón"]
}
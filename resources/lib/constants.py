# -*- coding: utf-8 -*-

VALID_FILECHARS = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

LANGUAGES = [
    'ar-AE', 'ar-SA', 'be-BY', 'bg-BG', 'bn-BD', 'ca-ES', 'ch-GU', 'cs-CZ', 'da-DK', 'de-AT', 'de-CH',
    'de-DE', 'el-GR', 'en-AU', 'en-CA', 'en-GB', 'en-IE', 'en-NZ', 'en-US', 'eo-EO', 'es-ES', 'es-MX',
    'et-EE', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'he-IL', 'hi-IN', 'hu-HU', 'id-ID',
    'it-IT', 'ja-JP', 'ka-GE', 'kk-KZ', 'kn-IN', 'ko-KR', 'lt-LT', 'lv-LV', 'ml-IN', 'ms-MY', 'ms-SG',
    'nb-NO', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'si-LK', 'sk-SK', 'sl-SI',
    'sr-RS', 'sv-SE', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'uk-UA', 'vi-VN', 'zh-CN', 'zh-HK',
    'zh-TW', 'zu-ZA']

TYPE_CONVERSION = {
    'movie': {
        'plural': 'Películas',
        'container': 'movies',
        'trakt': 'movie',
        'dbtype': 'movie'},
    'tv': {
        'plural': 'Series',
        'container': 'tvshows',
        'trakt': 'show',
        'dbtype': 'tvshow'},
    'person': {
        'plural': 'Personas',
        'container': 'actors',
        'trakt': '',
        'dbtype': 'video'},
    'review': {
        'plural': 'Reviews',
        'container': '',
        'trakt': '',
        'dbtype': ''},
    'image': {
        'plural': 'Imágenes',
        'container': 'images',
        'trakt': '',
        'dbtype': 'image'},
    'genre': {
        'plural': 'Géneros',
        'container': 'genres',
        'trakt': '',
        'dbtype': 'genre'},
    'season': {
        'plural': 'Temporadas',
        'container': 'seasons',
        'trakt': 'season',
        'dbtype': 'season'},
    'episode': {
        'plural': 'Episodios',
        'container': 'episodes',
        'trakt': 'episode',
        'dbtype': 'episode'},
    'video': {
        'plural': 'Videos',
        'container': 'videos',
        'trakt': '',
        'dbtype': 'video'}}

BASEDIR_MAIN = [
    {
        'info': 'dir_movie',
        'name': 'Movies',
        'spa': 'Películas',
        'icon': '{0}/resources/icons/tmdb/movies.png'},
    {
        'info': 'dir_tv',
        'name': 'TV Shows',
        'spa': 'Series',
        'icon': '{0}/resources/icons/tmdb/tv.png'},
    {
        'info': 'dir_person',
        'name': 'People',
        'spa': 'Personas',
        'icon': '{0}/resources/icons/tmdb/cast.png'},
    {
        'info': 'dir_random',
        'name': 'Randomised',
        'spa': 'Aleatorio',
        'icon': '{0}/resources/poster.png'},
    {
        'info': 'dir_discover',
        'name': 'Discover',
        'spa': 'Descubre',
        'icon': '{0}/resources/poster.png'},
    {
        'info': 'dir_tmdb',
        'name': 'TheMovieDb',
        'spa': 'TheMovieDb',
        'icon': '{0}/resources/poster.png'},
    {
        'info': 'dir_trakt',
        'name': 'Trakt',
        'spa': 'Trakt',
        'icon': '{0}/resources/trakt.png'}]

BASEDIR_TMDB = [
    {
        'info': 'dir_search',
        'name': 'Search{1}{0}',
        'spa': 'Buscar{1}{0}',
        'types': ['movie', 'tv', 'person'],
        'icon': '{0}/resources/icons/tmdb/search.png'},
    {
        'info': 'popular',
        'name': 'Popular{1}{0}',
        'spa': 'Popular{1}{0}',
        'types': ['movie', 'tv', 'person'],
        'icon': '{0}/resources/icons/tmdb/popular.png'},
    {
        'info': 'top_rated',
        'name': 'Top Rated{1}{0}',
        'spa': '{1}{0}Mejor Calificadas',
        'types': ['movie', 'tv'],
        'icon': '{0}/resources/icons/tmdb/toprated.png'},
    {
        'info': 'upcoming',
        'name': 'Upcoming{1}{0}',
        'spa': 'Próximas{1}{0}',
        'types': ['movie'],
        'icon': '{0}/resources/icons/tmdb/upcoming.png'},
    {
        'info': 'trending_day',
        'name': '{0}{1}Trending Today',
        'spa': '{0}{1}en Tendencia Hoy',
        'types': ['movie', 'tv', 'person'],
        'icon': '{0}/resources/icons/tmdb/upcoming.png'},
    {
        'info': 'trending_week',
        'name': '{0}{1}Trending This Week',
        'spa': '{0}{1}en Tendencia esta Semana',
        'types': ['movie', 'tv', 'person'],
        'icon': '{0}/resources/icons/tmdb/upcoming.png'},
    {
        'info': 'now_playing',
        'name': 'In Theatres',
        'spa': 'En Cines',
        'types': ['movie'],
        'icon': '{0}/resources/icons/tmdb/intheatres.png'},
    {
        'info': 'airing_today',
        'name': 'Airing Today',
        'spa': 'Al Aire Hoy',
        'types': ['tv'],
        'icon': '{0}/resources/icons/tmdb/airing.png'},
    {
        'info': 'on_the_air',
        'name': 'Currently Airing',
        'spa': 'Al Aire Actualmente',
        'types': ['tv'],
        'icon': '{0}/resources/icons/tmdb/airing.png'},
    {
        'info': 'genres',
        'name': '{0}{1}Genres',
        'spa': 'Géneros de {0}{1}',
        'types': ['movie', 'tv'],
        'icon': '{0}/resources/icons/tmdb/genre.png'},
    {
        'info': 'revenue_movies',
        'name': 'Highest Revenue{1}{0}',
        'spa': '{1}{0} con Éxito en Ganacias',
        'types': ['movie'],
        'icon': '{0}/resources/poster.png'},
    {
        'info': 'most_voted',
        'name': 'Most Voted{1}{0}',
        'spa': '{1}{0} Más Votadas',
        'types': ['movie', 'tv'],
        'icon': '{0}/resources/poster.png'}]

BASEDIR_TRAKT = [
    {
        'info': 'trakt_collection',
        'name': '{0}{1}Collection',
        'spa': '{0}{1}en Colección',
        'icon': '{0}/resources/icons/trakt/watchlist.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_watchlist',
        'name': '{0}{1}Watchlist',
        'spa': '{0}{1}en Watchlist',
        'icon': '{0}/resources/icons/trakt/watchlist.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_history',
        'name': 'Your Recently Watched{1}{0}',
        'spa': '{1}{0} Vistas Recientemente',
        'icon': '{0}/resources/icons/trakt/recentlywatched.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_mostwatched',
        'name': 'Your Most Watched{1}{0}',
        'spa': '{1}{0} más Vistas',
        'icon': '{0}/resources/icons/trakt/mostwatched.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_inprogress',
        'name': 'Your In-Progress{1}{0}',
        'spa': '{1}{0} en Progreso',
        'icon': '{0}/resources/icons/trakt/inprogress.png',
        'types': ['tv']},
    {
        'info': 'trakt_nextepisodes',
        'name': 'Your Next Episodes',
        'spa': 'Próximos Episodios',
        'icon': '{0}/resources/icons/trakt/inprogress.png',
        'types': ['tv']},
    {
        'info': 'trakt_recommendations',
        'name': '{0}{1}Recommended For You',
        'spa': '{0}{1}Recomendadas Para Ti',
        'icon': '{0}/resources/icons/trakt/recommended.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_becauseyouwatched',
        'name': 'Based on Recently Watched{1}{0}',
        'spa': 'Basadas en tus{1}{0} Vistas Recientemente',
        'icon': '{0}/resources/icons/trakt/recommended.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_becausemostwatched',
        'name': 'Based on Most Watched{1}{0}',
        'spa': 'Basadas en tus{1}{0} más Vistas',
        'icon': '{0}/resources/icons/trakt/recommended.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_myairing',
        'name': 'Your{1}{0}{1}Airing This Week',
        'spa': '{1}{0}{1}al Aire esta Semana',
        'icon': '{0}/resources/icons/trakt/airing.png',
        'types': ['tv']},
    {
        'info': 'trakt_calendar',
        'name': 'Your{1}{0}{1}Calendar',
        'spa': 'Tu Calendario de{1}{0}{1}',
        'icon': '{0}/resources/icons/trakt/calendar.png',
        'types': ['tv']},
    {
        'info': 'trakt_trending',
        'name': 'Trending{1}{0}',
        'spa': '{1}{0} en Tendencia',
        'icon': '{0}/resources/icons/trakt/trend.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_popular',
        'name': 'Popular{1}{0}',
        'spa': '{1}{0} Populares',
        'icon': '{0}/resources/icons/trakt/popular.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_mostplayed',
        'name': 'Most Played{1}{0}',
        'spa': '{1}{0} Más Vistas',
        'icon': '{0}/resources/icons/trakt/mostplayed.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_anticipated',
        'name': 'Anticipated{1}{0}',
        'spa': '{1}{0} Más Anticipadas',
        'icon': '{0}/resources/icons/trakt/anticipated.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_boxoffice',
        'name': 'Top 10 Box Office{1}{0}',
        'spa': '{1}{0} del Top 10 Box Office',
        'icon': '{0}/resources/icons/trakt/boxoffice.png',
        'types': ['movie']},
    {
        'info': 'trakt_trendinglists',
        'name': 'Trending Lists',
        'spa': 'Listas en Tendencia',
        'icon': '{0}/resources/icons/trakt/trendinglist.png',
        'types': ['both']},
    {
        'info': 'trakt_popularlists',
        'name': 'Popular Lists',
        'spa': 'Listas Populares',
        'icon': '{0}/resources/icons/trakt/popularlist.png',
        'types': ['both']},
    {
        'info': 'trakt_likedlists',
        'name': 'Liked Lists',
        'spa': 'Listas con tus Likes',
        'icon': '{0}/resources/icons/trakt/likedlist.png',
        'types': ['both']},
    {
        'info': 'trakt_mylists',
        'name': 'Your Lists',
        'spa': 'Tus Listas',
        'icon': '{0}/resources/icons/trakt/mylists.png',
        'types': ['both']}]

BASEDIR_RANDOM = [
    {
        'info': 'random_genres',
        'name': 'Random{1}{0}{1}Genre',
        'spa': 'Género Aleatorio de{1}{0}{1}',
        'types': ['movie', 'tv'],
        'icon': '{0}/resources/icons/tmdb/genre.png'},
    {
        'info': 'trakt_becauseyouwatched',
        'name': 'Based on Recently Watched{1}{0}',
        'spa': 'Basadas en {1}{0} Vistas Recientemente',
        'icon': '{0}/resources/icons/trakt/recommended.png',
        'types': ['movie', 'tv']},
    {
        'info': 'trakt_becausemostwatched',
        'name': 'Based on Most Watched{1}{0}',
        'spa': 'Basadas en{1}{0} Más Vistas',
        'icon': '{0}/resources/icons/trakt/recommended.png',
        'types': ['movie', 'tv']},
    {
        'info': 'random_trending',
        'name': 'Random Trending{1}{0}',
        'spa': '{1}{0} Aleatorias en Tendencia',
        'icon': '{0}/resources/icons/trakt/trend.png',
        'types': ['movie', 'tv']},
    {
        'info': 'random_popular',
        'name': 'Random Popular{1}{0}',
        'spa': '{1}{0}Populares Aleatorias',
        'icon': '{0}/resources/icons/trakt/popular.png',
        'types': ['movie', 'tv']},
    {
        'info': 'random_mostplayed',
        'name': 'Random Most Played{1}{0}',
        'spa': '{1}{0} Aleatorias Más Vistas',
        'icon': '{0}/resources/icons/trakt/mostplayed.png',
        'types': ['movie', 'tv']},
    {
        'info': 'random_anticipated',
        'name': 'Random Anticipated{1}{0}',
        'spa': '{1}{0} Aleatorias Más Anticipadas',
        'icon': '{0}/resources/icons/trakt/anticipated.png',
        'types': ['movie', 'tv']},
    {
        'info': 'random_trendinglists',
        'name': 'Random Trending List',
        'spa': 'Listas en Tendencia Aleatorias',
        'icon': '{0}/resources/icons/trakt/trendinglist.png',
        'types': ['both']},
    {
        'info': 'random_popularlists',
        'name': 'Random Popular List',
        'spa': 'Listas Populares Aleatorias',
        'icon': '{0}/resources/icons/trakt/popularlist.png',
        'types': ['both']},
    {
        'info': 'random_likedlists',
        'name': 'Random Liked List',
        'spa': 'Listas Aleatorias con Likes',
        'icon': '{0}/resources/icons/trakt/likedlist.png',
        'types': ['both']},
    {
        'info': 'random_mylists',
        'name': 'Random Your List',
        'spa': 'Tu Lista Aleatoria',
        'icon': '{0}/resources/icons/trakt/mylists.png',
        'types': ['both']}]

BASEDIR_DISCOVER = [
    {
        'info': 'user_discover',
        'name': 'Discover{1}{0}',
        'spa': 'Descubre{1}{0}',
        'types': ['movie', 'tv'],
        'icon': '{0}/resources/icons/tmdb/search.png'}]

BASEDIR_PATH = {
    'dir_movie': {
        'folders': [BASEDIR_TMDB, BASEDIR_TRAKT],
        'types': ['movie', 'both']},
    'dir_tv': {
        'folders': [BASEDIR_TMDB, BASEDIR_TRAKT],
        'types': ['tv', 'both']},
    'dir_person': {
        'folders': [BASEDIR_TMDB, BASEDIR_TRAKT],
        'types': ['person']},
    'dir_tmdb': {
        'folders': [BASEDIR_TMDB],
        'types': ['movie', 'tv', 'person', 'both']},
    'dir_trakt': {
        'folders': [BASEDIR_TRAKT],
        'types': ['movie', 'tv', 'person', 'both']},
    'dir_random': {
        'folders': [BASEDIR_RANDOM],
        'types': ['movie', 'tv', 'both']},
    'dir_discover': {
        'folders': [BASEDIR_DISCOVER],
        'types': ['movie', 'tv', 'both']}}

DETAILED_CATEGORIES = [
    {
        'info': 'cast',
        'name': 'Cast',
        'spa': 'Cast',
        'icon': '{0}/resources/icons/tmdb/cast.png',
        'types': ['movie', 'tv']},
    {
        'info': 'recommendations',
        'name': 'Recommended',
        'spa': 'Recomendadas',
        'icon': '{0}/resources/icons/tmdb/recommended.png',
        'types': ['movie', 'tv']},
    {
        'info': 'similar',
        'name': 'Similar',
        'spa': 'Similar',
        'icon': '{0}/resources/icons/tmdb/similar.png',
        'types': ['movie', 'tv']},
    {
        'info': 'crew',
        'name': 'Crew',
        'spa': 'Equipo',
        'icon': '{0}/resources/icons/tmdb/cast.png',
        'types': ['movie', 'tv']},
    {
        'info': 'posters',
        'name': 'Posters',
        'spa': 'Posters',
        'icon': '{0}/resources/icons/tmdb/images.png',
        'types': ['movie', 'tv']},
    {
        'info': 'fanart',
        'name': 'Fanart',
        'spa': 'Fanart',
        'icon': '{0}/resources/icons/tmdb/images.png',
        'types': ['movie', 'tv']},
    {
        'info': 'movie_keywords',
        'name': 'Keywords',
        'spa': 'Palabras Clave',
        'icon': '{0}/resources/icons/tmdb/tags.png',
        'types': ['movie']},
    {
        'info': 'reviews',
        'name': 'Reviews',
        'spa': 'Reseñas',
        'icon': '{0}/resources/icons/tmdb/reviews.png',
        'types': ['movie', 'tv']},
    {
        'info': 'stars_in_movies',
        'name': 'Cast in Movies',
        'spa': 'Cast en Películas',
        'icon': '{0}/resources/icons/tmdb/movies.png',
        'types': ['person']},
    {
        'info': 'stars_in_tvshows',
        'name': 'Cast in TV Shows',
        'spa': 'Cast en Series',
        'icon': '{0}/resources/icons/tmdb/tv.png',
        'types': ['person']},
    {
        'info': 'crew_in_movies',
        'name': 'Crew in Movies',
        'spa': 'Equipo en Películas',
        'icon': '{0}/resources/icons/tmdb/movies.png',
        'types': ['person']},
    {
        'info': 'crew_in_tvshows',
        'name': 'Crew in TV Shows',
        'spa': 'Equipo en Series',
        'icon': '{0}/resources/icons/tmdb/tv.png',
        'types': ['person']},
    {
        'info': 'images',
        'name': 'Images',
        'spa': 'Imágenes',
        'icon': '{0}/resources/icons/tmdb/images.png',
        'types': ['person']},
    {
        'info': 'seasons',
        'name': 'Seasons',
        'spa': 'Temporadas',
        'icon': '{0}/resources/icons/tmdb/episodes.png',
        'types': ['tv']},
    {
        'info': 'episode_cast',
        'name': 'Cast',
        'spa': 'Cast',
        'icon': '{0}/resources/icons/tmdb/cast.png',
        'types': ['episode']},
    {
        'info': 'episode_thumbs',
        'name': 'Thumbs',
        'spa': 'Miniaturas',
        'icon': '{0}/resources/icons/tmdb/images.png',
        'types': ['episode']},
    {
        'info': 'videos',
        'name': 'Videos',
        'spa': 'Videos',
        'icon': '{0}/resources/icons/tmdb/movies.png',
        'types': ['movie', 'tv', 'episode']},
    {
        'info': 'trakt_inlists',
        'name': 'In Trakt Lists',
        'spa': 'Listas en Trakt',
        'icon': '{0}/resources/icons/tmdb/trakt.png',
        'url_key': 'imdb_id',
        'types': ['movie', 'tv']}]

RANDOM_LISTS = {
    'random_genres': 'genres',
    'random_trendinglists': 'trakt_trendinglists',
    'random_popularlists': 'trakt_popularlists',
    'random_likedlists': 'trakt_likedlists',
    'random_mylists': 'trakt_mylists'}

RANDOM_TRAKT = {
    'random_trending': 'trakt_trending',
    'random_popular': 'trakt_popular',
    'random_mostplayed': 'trakt_mostplayed',
    'random_anticipated': 'trakt_anticipated'}

TMDB_LISTS = {
    'search': {
        'path': 'search/{type}',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'popular': {
        'path': '{type}/popular',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'top_rated': {
        'path': '{type}/top_rated',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'upcoming': {
        'path': '{type}/upcoming',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'trending_day': {
        'path': 'trending/{type}/day',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'trending_week': {
        'path': 'trending/{type}/week',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'now_playing': {
        'path': '{type}/now_playing',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'airing_today': {
        'path': '{type}/airing_today',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'on_the_air': {
        'path': '{type}/on_the_air',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'genres': {
        'path': 'genre/{type}/list',
        'key': 'genres',
        'url_info': 'genre',
        'url_type': '{type}',
        'item_tmdbtype': 'genre'},
    'discover': {
        'path': 'discover/{type}',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'genre': {
        'path': 'discover/{type}',
        'key': 'results',
        'url_info': 'details',
        'url_ext': 'with_genres={tmdb_id}',
        'item_tmdbtype': '{type}'},
    'recommendations': {
        'path': '{type}/{tmdb_id}/recommendations',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'similar': {
        'path': '{type}/{tmdb_id}/similar',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'movie_keywords': {
        'path': '{type}/{tmdb_id}/keywords',
        'key': 'keywords',
        'url_info': 'keyword_movies',
        'url_type': 'movie',
        'item_tmdbtype': 'keyword'},
    'reviews': {
        'path': '{type}/{tmdb_id}/reviews',
        'key': 'results',
        'url_info': 'textviewer',
        'item_tmdbtype': 'review'},
    'posters': {
        'path': '{type}/{tmdb_id}/images',
        'key': 'posters',
        'url_info': 'imageviewer',
        'item_tmdbtype': 'image'},
    'fanart': {
        'path': '{type}/{tmdb_id}/images',
        'key': 'backdrops',
        'url_info': 'imageviewer',
        'item_tmdbtype': 'image'},
    'seasons': {
        'path': '{type}/{tmdb_id}',
        'key': 'seasons',
        'url_info': 'episodes',
        'url_tmdb_id': '{tmdb_id}',
        'item_tmdbtype': 'season'},
    'episode_cast': {
        'path': 'tv/{tmdb_id}/season/{season}/episode/{episode}/credits',
        'key': 'cast',
        'url_info': 'details',
        'url_tmdb_id': '{tmdb_id}',
        'item_tmdbtype': 'person'},
    'episode_thumbs': {
        'path': 'tv/{tmdb_id}/season/{season}/episode/{episode}/images',
        'key': 'stills',
        'url_info': 'imageviewer',
        'url_tmdb_id': '{tmdb_id}',
        'item_tmdbtype': 'image'},
    'stars_in_movies': {
        'path': 'person/{tmdb_id}/movie_credits',
        'key': 'cast',
        'url_info': 'details',
        'item_tmdbtype': 'movie'},
    'stars_in_tvshows': {
        'path': 'person/{tmdb_id}/tv_credits',
        'key': 'cast',
        'url_info': 'details',
        'item_tmdbtype': 'tv'},
    'crew_in_movies': {
        'path': 'person/{tmdb_id}/movie_credits',
        'key': 'crew',
        'url_info': 'details',
        'item_tmdbtype': 'movie'},
    'crew_in_tvshows': {
        'path': 'person/{tmdb_id}/tv_credits',
        'key': 'crew',
        'url_info': 'details',
        'item_tmdbtype': 'tv'},
    'videos': {
        'path': '{type}/{tmdb_id}/videos',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': 'video'},
    'images': {
        'path': 'person/{tmdb_id}/images',
        'key': 'profiles',
        'url_info': 'imageviewer',
        'item_tmdbtype': 'image'},
    'collection': {
        'path': 'collection/{tmdb_id}',
        'tmdb_check_id': 'collection',
        'key': 'parts',
        'url_info': 'details',
        'item_tmdbtype': 'movie'},
    'keyword_movies': {
        'path': 'keyword/{tmdb_id}/movies',
        'key': 'results',
        'url_info': 'details',
        'item_tmdbtype': '{type}'},
    'revenue_movies': {
        'path': 'discover/{type}',
        'key': 'results',
        'url_info': 'details',
        'url_ext': 'sort_by=revenue.desc',
        'item_tmdbtype': '{type}'},
    'most_voted': {
        'path': 'discover/{type}',
        'key': 'results',
        'url_info': 'details',
        'url_ext': 'sort_by=vote_count.desc',
        'item_tmdbtype': '{type}'},
    'episodes': {
        'path': 'tv/{tmdb_id}/season/{season}',
        'key': 'episodes',
        'url_info': 'details',
        'url_tmdb_id': '{tmdb_id}',
        'item_tmdbtype': 'episode'}}

APPEND_TO_RESPONSE = 'credits,images,release_dates,content_ratings,external_ids,videos,movie_credits,tv_credits'

TRAKT_LISTS = {
    'trakt_watchlist': {
        'path': 'users/{user_slug}/watchlist/{type}/{sortmethod}',
        'req_auth': True,
        'item_tmdbtype': '{type}'},
    'trakt_recommendations': {
        'path': 'recommendations/{type}?ignore_collected=true',
        'req_auth': True,
        'item_tmdbtype': '{type}'},
    'trakt_trending': {
        'path': '{type}/trending',
        'item_tmdbtype': '{type}'},
    'trakt_popular': {
        'path': '{type}/popular',
        'item_tmdbtype': '{type}'},
    'trakt_mostplayed': {
        'path': '{type}/played/weekly',
        'item_tmdbtype': '{type}'},
    'trakt_anticipated': {
        'path': '{type}/anticipated',
        'item_tmdbtype': '{type}'},
    'trakt_boxoffice': {
        'path': '{type}/boxoffice',
        'item_tmdbtype': '{type}'},
    'trakt_userlist': {
        'path': 'users/{user_slug}/lists/{list_slug}/items',
        'item_tmdbtype': '{type}'},
    'trakt_trendinglists': {
        'path': 'lists/trending',
        'item_tmdbtype': '{type}'},
    'trakt_popularlists': {
        'path': 'lists/popular',
        'item_tmdbtype': '{type}'},
    'trakt_likedlists': {
        'path': 'users/likes/lists',
        'req_auth': True,
        'item_tmdbtype': '{type}'},
    'trakt_mylists': {
        'path': 'users/{user_slug}/lists',
        'req_auth': True,
        'item_tmdbtype': '{type}'},
    'trakt_inlists': {
        'path': 'movies/{imdb_id}/lists',
        'url_key': 'imdb_id',
        'item_tmdbtype': '{type}'},
    'trakt_myairing': {
        'path': 'calendars/my/{type}',
        'req_auth': True,
        'item_tmdbtype': '{type}'},
    'trakt_airing': {
        'path': 'calendars/all/{type}',
        'item_tmdbtype': '{type}'},
    'trakt_premiering': {
        'path': 'calendars/all/{type}/premieres',
        'item_tmdbtype': '{type}'}}

TRAKT_MANAGEMENT = ['collection_add', 'collection_remove', 'watchlist_add', 'watchlist_remove', 'history_add', 'history_remove']

TRAKT_USERLISTS = ['trakt_mylists', 'trakt_trendinglists', 'trakt_popularlists', 'trakt_likedlists', 'trakt_inlists']

TRAKT_HISTORY = ['trakt_nextepisodes', 'trakt_inprogress', 'trakt_history', 'trakt_mostwatched']

TRAKT_CALENDAR = [
    ('Last Fortnight', -14, 14), ('Last Week', -7, 7), ('Yesterday', -1, 1), ('Today', 0, 1), ('Tomorrow', 1, 1),
    ('{0}', 2, 1), ('{0}', 3, 1), ('{0}', 4, 1), ('{0}', 5, 1), ('{0}', 6, 1), ('Next Week', 0, 7)]

USER_DISCOVER_LISTITEMS_BASEDIR = [
    {'label': 'Discover {0} w/ Below Settings', 'url': {'info': 'user_discover', 'method': 'open'}},
    {'label': 'Match Method', 'url': {'info': 'user_discover', 'method': 'with_separator'}},
    {'label': 'Sort Method', 'url': {'info': 'user_discover', 'method': 'sort_by'}}]

USER_DISCOVER_LISTITEMS_ADDRULE = [
    {'label': 'Clear Settings', 'url': {'info': 'user_discover', 'method': 'clear'}},
    {'label': 'Add Rule...', 'url': {'info': 'user_discover', 'method': 'add_rule'}}]

USER_DISCOVER_LISTITEMS_START = [
    {'label': 'With Genres', 'url': {'info': 'user_discover', 'method': 'with_genres'}},
    {'label': 'Without Genres', 'url': {'info': 'user_discover', 'method': 'without_genres'}},
    {'label': 'With Companies', 'url': {'info': 'user_discover', 'method': 'with_companies'}},
    {'label': 'With Keywords', 'url': {'info': 'user_discover', 'method': 'with_keywords'}},
    {'label': 'Without Keywords', 'url': {'info': 'user_discover', 'method': 'without_keywords'}}]

USER_DISCOVER_LISTITEMS_FINISH = [
    {'label': 'Vote Count ( > or = )', 'url': {'info': 'user_discover', 'method': 'vote_count.gte'}},
    {'label': 'Vote Count ( < or = )', 'url': {'info': 'user_discover', 'method': 'vote_count.lte'}},
    {'label': 'Vote Average ( > or = )', 'url': {'info': 'user_discover', 'method': 'vote_average.gte'}},
    {'label': 'Vote Average ( < or = )', 'url': {'info': 'user_discover', 'method': 'vote_average.lte'}},
    {'label': 'Runtime (Minutes) ( > or = )', 'url': {'info': 'user_discover', 'method': 'with_runtime.gte'}},
    {'label': 'Runtime (Minutes) ( < or = )', 'url': {'info': 'user_discover', 'method': 'with_runtime.lte'}}]

USER_DISCOVER_LISTITEMS_MOVIES = USER_DISCOVER_LISTITEMS_START + [
    {'label': 'With Cast', 'url': {'info': 'user_discover', 'method': 'with_cast'}},
    {'label': 'With Crew', 'url': {'info': 'user_discover', 'method': 'with_crew'}},
    {'label': 'With People', 'url': {'info': 'user_discover', 'method': 'with_people'}},
    {'label': 'Primary Release Year', 'url': {'info': 'user_discover', 'method': 'primary_release_year'}},
    {'label': 'Primary Release Date ( > or = )', 'url': {'info': 'user_discover', 'method': 'primary_release_date.gte'}},
    {'label': 'Primary Release Date ( < or = )', 'url': {'info': 'user_discover', 'method': 'primary_release_date.lte'}},
    {'label': 'Release Date ( > or = )', 'url': {'info': 'user_discover', 'method': 'release_date.gte'}},
    {'label': 'Release Date ( < or = )', 'url': {'info': 'user_discover', 'method': 'release_date.lte'}},
    {'label': 'Release Type', 'url': {'info': 'user_discover', 'method': 'with_release_type'}}] + USER_DISCOVER_LISTITEMS_FINISH

USER_DISCOVER_LISTITEMS_TVSHOWS = USER_DISCOVER_LISTITEMS_START + [
    {'label': 'With Networks', 'url': {'info': 'user_discover', 'method': 'with_networks'}},
    {'label': 'Air Date ( > or = )', 'url': {'info': 'user_discover', 'method': 'air_date.gte'}},
    {'label': 'Air Date ( < or = )', 'url': {'info': 'user_discover', 'method': 'air_date.lte'}},
    {'label': 'First Air Date ( > or = )', 'url': {'info': 'user_discover', 'method': 'first_air_date.gte'}},
    {'label': 'First Air Date ( < or = )', 'url': {'info': 'user_discover', 'method': 'first_air_date.lte'}},
    {'label': 'First Air Year', 'url': {'info': 'user_discover', 'method': 'first_air_date_year'}}] + USER_DISCOVER_LISTITEMS_FINISH

USER_DISCOVER_SORTBY_MOVIES = [
    'popularity.asc', 'popularity.desc', 'release_date.asc', 'release_date.desc', 'revenue.asc', 'revenue.desc',
    'primary_release_date.asc', 'primary_release_date.desc', 'original_title.asc', 'original_title.desc',
    'vote_average.asc', 'vote_average.desc', 'vote_count.asc', 'vote_count.desc']

USER_DISCOVER_SORTBY_TVSHOWS = [
    'vote_average.desc', 'vote_average.asc', 'first_air_date.desc', 'first_air_date.asc', 'popularity.desc', 'popularity.asc']

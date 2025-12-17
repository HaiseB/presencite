console.log('presencetableau.js chargé');

// Fonctions utilitaires pour les cookies
function setCookie(name, value, days) {
    let expires = '';
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = '; expires=' + date.toUTCString();
    }
    document.cookie = name + '=' + (value || '') + expires + '; path=/';
}

function getCookie(name) {
    const nameEQ = name + '=';
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

document.addEventListener('DOMContentLoaded', function () {
    const switchDetaille = document.getElementById('switchModeDetaille');
    function toggleLignesDetaillees() {
        const lignes = document.querySelectorAll('.ligne-detaillee');
        lignes.forEach(ligne => {
            ligne.style.display = switchDetaille.checked ? '' : 'none';
        });
        setCookie('modeDetaille', switchDetaille.checked ? '1' : '0', 30);
    }
    if (switchDetaille) {
        // Restaure l'état du switch depuis le cookie
        const modeDetailleCookie = getCookie('modeDetaille');
        if (modeDetailleCookie !== null) {
            switchDetaille.checked = modeDetailleCookie === '1';
        }
        switchDetaille.addEventListener('change', toggleLignesDetaillees);
        toggleLignesDetaillees(); // état initial
    }

    // Gestion du switch pour afficher/masquer les infos de présences (validation et non remplis)
    const switchInfosPresences = document.getElementById('switchAfficherInfosPresences');
    const infosPresencesContainer = document.getElementById('infos-presences-container');
    function toggleInfosPresences() {
        if (infosPresencesContainer && switchInfosPresences) {
            infosPresencesContainer.style.display = switchInfosPresences.checked ? '' : 'none';
            setCookie('afficherInfosPresences', switchInfosPresences.checked ? '1' : '0', 30);
        }
    }
    if (switchInfosPresences && infosPresencesContainer) {
        // Restaure l'état du switch depuis le cookie (par défaut décoché = '0')
        const afficherInfosPresencesCookie = getCookie('afficherInfosPresences');
        if (afficherInfosPresencesCookie !== null) {
            switchInfosPresences.checked = afficherInfosPresencesCookie === '1';
        } else {
            // Par défaut : décoché
            switchInfosPresences.checked = false;
        }
        switchInfosPresences.addEventListener('change', toggleInfosPresences);
        toggleInfosPresences(); // état initial
    }
});
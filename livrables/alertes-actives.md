# Alertes actives — Veille Sentiers Europe (pilote)

REGISTRE PERSISTANT. État courant des restrictions/changements sur les sentiers du périmètre
pilote (France + Caminos ES). Mémoire de l'agent veille-europe : sert à ne remonter dans le
digest QUE le NOUVEAU ou le CHANGÉ. Les items inchangés voient seulement leur « Dernière
vérif » mise à jour. Les items expirés/levés passent en [CLÔTURÉ] (date), pas supprimés.
*Amorcé le 2026-07-17 par import du registre de la veille OMW (mêmes alertes France).*

**Clé** = `type|zone|objet|date-d'effet` (stable d'un run à l'autre).

| Clé | Type | Portion concernée | Alternative | Zone (détails) | Itinéraires | Sévérité | Validité | 1ère détection | Dernière vérif | Source | Statut |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|

# -*- coding: utf-8 -*-
"""Abrechnungsfrist-Rechner: Abrechnungsfrist (§ 556 Abs. 3 S. 2 BGB) und Einwendungsfrist (S. 5)."""
META = {
    "slug": "abrechnungsfrist-rechner",
    "name": "Abrechnungsfrist-Rechner",
    "title": "Abrechnungsfrist-Rechner: Bis wann muss die Nebenkostenabrechnung beim Mieter sein?",
    "description": "Abrechnungsfrist und Einwendungsfrist der Nebenkostenabrechnung nach § 556 BGB berechnen – mit Ampel, wie viele Tage noch bleiben. Kostenlos, ohne Anmeldung.",
    "card_text": "Bis wann muss die Abrechnung beim Mieter sein – und wie lange darf er widersprechen?",
    "llms": "Rechner für die Abrechnungsfrist (12 Monate nach Ende des Abrechnungszeitraums, maßgeblich ist der Zugang beim Mieter) und die Einwendungsfrist des Mieters (bis Ende des 12. Monats nach Zugang), § 556 Abs. 3 BGB.",
    "date": "2026-10-30",
    "eyebrow": "Kostenloser Rechner · § 556 BGB",
    "answer": "Die Nebenkostenabrechnung muss dem Mieter **spätestens 12 Monate nach Ende des Abrechnungszeitraums zugehen** – für das Kalenderjahr 2025 also bis zum 31.12.2026. Entscheidend ist der Zugang, nicht das Absenden.",
    "order": 1,
    "faq": [
        ("Was passiert, wenn ich die Frist verpasse?", "Eine Nachzahlung können Sie dann in der Regel nicht mehr verlangen (§ 556 Abs. 3 S. 3 BGB). Ein Guthaben des Mieters müssen Sie trotzdem auszahlen. Ausnahme: Sie haben die Verspätung nicht zu vertreten, etwa weil der Versorger seine Rechnung verspätet geschickt hat."),
        ("Reicht es, wenn ich die Abrechnung am 31.12. einwerfe?", "Nur wenn sie an diesem Tag noch zu den üblichen Zeiten in den Briefkasten kommt, sodass mit einer Leerung am selben Tag zu rechnen ist. Ein Einwurf spät am Silvesterabend gilt erst im neuen Jahr als zugegangen. Planen Sie lieber zwei Wochen Puffer ein und dokumentieren Sie den Zugang (Bote, Einwurf-Einschreiben)."),
        ("Wie lange kann der Mieter Einwendungen erheben?", "Bis zum Ablauf des zwölften Monats nach Zugang der Abrechnung (§ 556 Abs. 3 S. 5 BGB). Geht die Abrechnung am 15.03.2026 zu, kann der Mieter bis zum 31.03.2027 widersprechen."),
        ("Wird meine Eingabe gespeichert?", "Nein. Der Rechner rechnet nur in Ihrem Browser, es wird nichts übertragen."),
    ],
    "sources": [
        ("§ 556 BGB – Vereinbarungen über Betriebskosten (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__556.html"),
    ],
}

BODY = """<form class="calc" id="calc" onsubmit="return false">
<div class="row2">
<div><label for="ende">Ende des Abrechnungszeitraums</label><input type="date" id="ende" value="2025-12-31"></div>
<div><label for="zug">Zugang beim Mieter (optional)</label><input type="date" id="zug" value=""></div>
</div>
<p class="hint">Meist endet der Abrechnungszeitraum am 31.12. Tragen Sie das Zugangsdatum ein, wenn die Abrechnung schon verschickt ist.</p>
<div class="res" id="res" aria-live="polite"></div>
</form>"""

EXPLAIN = """<h2 class="serif" style="margin-top:0">So rechnet der Rechner</h2>
<p><strong>Abrechnungsfrist:</strong> Die Abrechnung muss dem Mieter spätestens bis zum Ablauf des zwölften Monats nach Ende des Abrechnungszeitraums zugehen (§ 556 Abs. 3 S. 2 BGB). Endet der Zeitraum nicht am Monatsende, rechnet der Rechner vorsichtig mit genau 12 Monaten.</p>
<p><strong>Einwendungsfrist:</strong> Der Mieter kann Einwendungen bis zum Ablauf des zwölften Monats nach Zugang erheben (§ 556 Abs. 3 S. 5 BGB).</p>
<p><strong>Ampel:</strong> Grün bei mehr als 8 Wochen Restzeit, Gelb bis 8 Wochen, Rot bei 14 Tagen oder weniger.</p>
<p class="note">Allgemeine Information, keine Rechtsberatung. Im Einzelfall helfen Haus &amp; Grund, Mieterverein oder Anwalt.</p>"""

SCRIPT = r"""
function pd(v){if(!v)return null;var p=v.split('-');return new Date(+p[0],+p[1]-1,+p[2])}
function de(d){return ('0'+d.getDate()).slice(-2)+'.'+('0'+(d.getMonth()+1)).slice(-2)+'.'+d.getFullYear()}
function eom(y,m){return new Date(y,m+1,0)}
function frist(e){var n=new Date(e.getFullYear(),e.getMonth(),e.getDate()+1);
 if(n.getDate()===1)return eom(e.getFullYear(),e.getMonth()+12);
 var t=new Date(e.getFullYear(),e.getMonth()+12,e.getDate());
 if(t.getDate()!==e.getDate())t=eom(e.getFullYear(),e.getMonth()+12);return t}
function calc(){var e=pd($('ende').value),z=pd($('zug').value),r=$('res');
 if(!e){r.innerHTML=light('y','Bitte das Ende des Abrechnungszeitraums eingeben.');return}
 var f=frist(e),h=new Date();h.setHours(0,0,0,0);var tage=Math.round((f-h)/864e5),out='';
 if(z){var ok=z<=f;
  out+=ok?light('g','Rechtzeitig: Zugang am '+de(z)+', Frist bis '+de(f)+'.')
         :light('r','Zu spät: Zugang am '+de(z)+', die Frist lief am '+de(f)+' ab.','Eine Nachzahlung kann dann meist nicht mehr verlangt werden; ein Guthaben ist trotzdem auszuzahlen.');
  var ew=eom(z.getFullYear(),z.getMonth()+12);
  out+='<div class="kpis"><div class="kpi"><span>Abrechnungsfrist</span><b>'+de(f)+'</b></div><div class="kpi"><span>Einwendungen bis</span><b>'+de(ew)+'</b></div></div>';
 }else{
  if(tage<0)out+=light('r','Die Frist ist am '+de(f)+' abgelaufen.','Nachzahlungen können meist nicht mehr verlangt werden; Guthaben sind trotzdem auszuzahlen.');
  else if(tage<=14)out+=light('r','Nur noch '+tage+' Tage: Die Abrechnung muss bis '+de(f)+' beim Mieter sein.','Zustellung per Bote oder persönlich – und den Zugang dokumentieren.');
  else if(tage<=56)out+=light('y','Noch '+tage+' Tage bis zum '+de(f)+'.','Jetzt die Belege zusammenstellen.');
  else out+=light('g','Noch '+tage+' Tage Zeit – Frist bis '+de(f)+'.');
  out+='<div class="kpis"><div class="kpi"><span>Zugang spätestens</span><b>'+de(f)+'</b></div><div class="kpi"><span>Restzeit</span><b>'+(tage<0?'abgelaufen':tage+' Tage')+'</b></div></div>';
 }
 r.innerHTML=out;}
['ende','zug'].forEach(function(i){$(i).addEventListener('input',calc)});calc();
"""

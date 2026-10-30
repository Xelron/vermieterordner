# -*- coding: utf-8 -*-
"""Heizkosten-Rechner: Aufteilung nach Verbrauch und Fläche (§ 7 HeizkostenV)."""
META = {
    "slug": "heizkosten-rechner",
    "name": "Heizkosten-Rechner",
    "title": "Heizkosten-Rechner: Heizkosten nach Verbrauch und Fläche aufteilen (70/30, 60/40, 50/50)",
    "description": "Heizkostenanteil einer Wohnung nach Heizkostenverordnung berechnen: Grundkosten nach Wohnfläche, Verbrauchskosten nach Zählerwerten – kostenlos im Browser.",
    "card_text": "Heizkostenanteil einer Wohnung nach 70/30, 60/40 oder 50/50 berechnen.",
    "llms": "Rechner für die Heizkostenaufteilung nach § 7 HeizkostenV: Verbrauchsanteil 50–70 % nach erfasstem Verbrauch (Einheiten oder kWh), Rest nach Wohnfläche; optional zeitanteilig bei Mieterwechsel.",
    "date": "2026-10-30",
    "seo_title": "Heizkosten-Rechner: Heizkosten aufteilen (70/30, 50/50) | Vermieterordner",
    "eyebrow": "Kostenloser Rechner · HeizkostenV",
    "answer": "**Heizkostenanteil = Verbrauchskosten + Grundkosten.** Bei 70/30 und 4.000 € Heizkosten: 2.800 € werden nach Verbrauch verteilt, 1.200 € nach Wohnfläche. Wer 4.120 von 9.860 Einheiten verbraucht und 85 von 230 m² bewohnt, zahlt 1.169,98 € + 443,48 € = 1.613,46 €.",
    "order": 2,
    "faq": [
        ("Wann sind 70 % nach Verbrauch Pflicht?", "Wenn das Haus die Anforderungen der Wärmeschutzverordnung von 1994 nicht erfüllt, mit Öl oder Gas beheizt wird und die freiliegenden Heizungsleitungen überwiegend gedämmt sind (§ 7 Abs. 1 S. 2 HeizkostenV). Sonst wählen Sie einen Anteil zwischen 50 und 70 %."),
        ("Was gehört zu den Heizkosten?", "Brennstoff bzw. Wärmelieferung, Betriebsstrom, Wartung, Reinigung, Abgasmessung, Miete und Eichung der Messgeräte sowie Ablesung und Abrechnung (§ 7 Abs. 2 HeizkostenV)."),
        ("Und das Warmwasser?", "Bereitet die Heizung auch das Warmwasser, müssen die Kosten vorher getrennt werden (§ 9 HeizkostenV). Diesen Rechner verwenden Sie dann für den Heizungsanteil; der Warmwasseranteil wird genauso, aber nach Warmwasserzählern verteilt."),
        ("Wird meine Eingabe gespeichert?", "Nein. Der Rechner rechnet nur in Ihrem Browser, es wird nichts übertragen."),
    ],
    "sources": [
        ("§ 7 HeizkostenV – Verteilung der Kosten der Versorgung mit Wärme (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/heizkostenv/__7.html"),
        ("§ 9b HeizkostenV – Kostenaufteilung bei Nutzerwechsel (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/heizkostenv/__9b.html"),
    ],
}

BODY = """<form class="calc" id="calc" onsubmit="return false">
<div class="row2">
<div><label for="hk">Heizkosten gesamt (€)</label><input type="text" id="hk" inputmode="decimal" value="4000" autocomplete="off"></div>
<div><label for="va">Verbrauchsanteil</label><select id="va"><option value="70" selected>70/30 (70 % Verbrauch)</option><option value="60">60/40</option><option value="50">50/50</option></select></div>
</div>
<div class="row2">
<div><label for="fg">Wohnfläche Haus gesamt (m²)</label><input type="text" id="fg" inputmode="decimal" value="230" autocomplete="off"></div>
<div><label for="fw">Wohnfläche der Wohnung (m²)</label><input type="text" id="fw" inputmode="decimal" value="85" autocomplete="off"></div>
</div>
<div class="row2">
<div><label for="vg">Verbrauch Haus gesamt (Einheiten/kWh)</label><input type="text" id="vg" inputmode="decimal" value="9860" autocomplete="off"></div>
<div><label for="vw">Verbrauch der Wohnung</label><input type="text" id="vw" inputmode="decimal" value="4120" autocomplete="off"></div>
</div>
<div class="row2">
<div><label for="tw">Nutzungstage (bei Mieterwechsel)</label><input type="text" id="tw" inputmode="numeric" value="365" autocomplete="off"></div>
<div><label for="tz">Tage im Abrechnungszeitraum</label><input type="text" id="tz" inputmode="numeric" value="365" autocomplete="off"></div>
</div>
<p class="hint">Gesamtfläche immer mit leeren und selbst genutzten Wohnungen – deren Anteil trägt der Vermieter. Gesamtverbrauch = Summe aller Wohnungen.</p>
<div class="res" id="res" aria-live="polite"></div>
</form>"""

EXPLAIN = """<h2 class="serif" style="margin-top:0">So rechnet der Rechner</h2>
<p><strong>Verbrauchskosten</strong> = Heizkosten × Verbrauchsanteil × Verbrauch der Wohnung ÷ Verbrauch gesamt</p>
<p><strong>Grundkosten</strong> = Heizkosten × (1 − Verbrauchsanteil) × Fläche der Wohnung ÷ Gesamtfläche × Nutzungstage ÷ Tage im Zeitraum</p>
<p>Bei Mieterwechsel werden die Grundkosten zeitanteilig verteilt, die Verbrauchskosten nach der Zwischenablesung (§ 9b HeizkostenV). Die Heizkostenverordnung erlaubt für die Grundkosten auch eine Verteilung nach Gradtagszahlen.</p>
<p>Schritt für Schritt: <a href="nebenkostenabrechnung-erstellen.html">Nebenkostenabrechnung erstellen</a>.</p>
<p class="note">Vereinfachte Rechnung ohne Warmwassertrennung und ohne CO2-Kostenaufteilung. Allgemeine Information, keine Rechtsberatung.</p>"""

SCRIPT = r"""
function calc(){var hk=num($('hk').value),va=+$('va').value/100,fg=num($('fg').value),fw=num($('fw').value),vg=num($('vg').value),vw=num($('vw').value),tw=num($('tw').value),tz=num($('tz').value),r=$('res');
 var raw=['hk','fg','fw','vg','vw','tw','tz'].map(function(i){return $(i).value});
 if(raw.some(function(v){return !/^[\s\d.,€]*$/.test(v)})||[hk,fg,fw,vg,vw,tw,tz].some(function(x){return x===null})){r.innerHTML=light('y','Bitte alle Felder mit Zahlen füllen.');return}
 if([hk,fg,fw,vg,vw,tw,tz].some(function(x){return x<0})){r.innerHTML=light('y','Bitte nur Zahlen ab 0 eingeben – negative Werte sind nicht möglich.');return}
 if(fg<=0||vg<=0||tz<=0){r.innerHTML=light('y','Gesamtfläche, Gesamtverbrauch und Tage im Zeitraum müssen größer als 0 sein.');return}
 if(fw>fg){r.innerHTML=light('r','Die Wohnfläche der Wohnung ist größer als die Gesamtfläche.');return}
 if(vw>vg){r.innerHTML=light('r','Der Verbrauch der Wohnung ist größer als der Gesamtverbrauch.');return}
 if(tw>tz){r.innerHTML=light('r','Die Nutzungstage sind mehr als die Tage im Zeitraum.');return}
 var v=Math.round(hk*va*vw/vg*100)/100,g=Math.round(hk*(1-va)*fw/fg*tw/tz*100)/100,s=v+g;
 r.innerHTML='<div class="kpis"><div class="kpi"><span>Verbrauchskosten</span><b>'+eur(v)+'</b></div>'
  +'<div class="kpi"><span>Grundkosten</span><b>'+eur(g)+'</b></div>'
  +'<div class="kpi"><span>Heizkosten der Wohnung</span><b>'+eur(s)+'</b></div></div>'
  +'<p class="hint">Anteil an den gesamten Heizkosten: '+fmt(hk>0?s/hk*100:0,1)+' %</p>';
}
['hk','va','fg','fw','vg','vw','tw','tz'].forEach(function(i){$(i).addEventListener('input',calc)});calc();
"""

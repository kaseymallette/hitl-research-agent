T = {}
T["T1"] = """Figure 1 (schematic; labels and flow as read from the page image). Labeled elements: Scope-1 Water group containing a tap/water-supply icon feeding a "Cooling Tower" (blue arrows: supply water flows into the cooling tower and onward to the "Heat Exchanger"; a red pump/fan symbol links the cooling tower to the heat exchanger loop). Heat Exchanger: a coil between the cooling-tower loop and the data-center loop. In the data-center loop: "Warm Water" (red arrow) returns from the "CRAH" (computer room air handler, drawn as a tall blue unit inside the "Data Center" platform) to the heat exchanger, and "Chilled Water" (blue arrow) returns from the heat exchanger to the CRAH. On the data-center platform: "Server Rack" with icons labeled BLOOM, Meta OPT-175B, ChatGPT and AlphaGO. Scope-2 Water group: a "Power Plant" (grey, with transmission towers carrying electricity to the data center) cooling via a "Cooling Tower" (a second, separate cooling tower) with a red arrow from that cooling tower to a "Water Source" (lake icon). The caption states the model icons are only for illustration."""
T["T1_caveat"] = ("the figure is a qualitative schematic with no numeric data. The direction of every arrow and whether the "
                  "tap icon represents a municipal supply or another source are my reading of the drawing, not stated in the text.")
T["T2"] = """Figure 2 (three charts; approximate values read visually from the page image; the PDF text layer holds only axis tick labels).
(a) Carbon/water efficiency: scatter of U.S. eGRID subregions. X axis: Carbon (kg/kWh), ticks 0.1, 0.3, 0.5, 0.7, 0.9. Y axis: Water (L/kWh), ticks 0, 4, 8, 12, 16. Labeled points (approximate): AKMS about (0.22, 15.3); NWPP about (0.29, 9.6); NYUP about (0.10, 8.1); AZNM about (0.37, 5.0); MROE about (0.72, 3.0); HIOA about (0.73, 1.4). About twenty further unlabeled points lie roughly between carbon 0.24 and 0.70 and water 1.4 and 5.3. A dashed orange regression line falls from about 8 L/kWh at carbon 0 to about 0 L/kWh near carbon 0.75 (negative slope). Per the caption, the carbon and water efficiencies are not aligned.
(b) Hourly carbon/water efficiency, Virginia, five days (MON to FRI) from Apr. 4, 2022. Left axis, blue line: Water (L/kWh), range 1.5 to 3.0. Right axis, orange line: Carbon (kg/kWh), range 0.20 to 0.40. The blue water-intensity line shows repeated daily spikes to roughly 2.3 to 2.6 L/kWh against a baseline of roughly 1.7 to 1.9; the orange carbon line stays roughly between 0.31 and 0.37 kg/kWh with smaller swings. The caption gives a Pearson correlation coefficient of 0.06 between them.
(c) Hourly energy fuel mixes serving Virginia, same five days. Y axis: Percentage, ticks 0, 20, 40, 60. Legend: Coal (blue), Natural Gas (orange), Nuclear (green), Oil (red), Wind (grey), Solar (brown), Hydro (pink), Other (purple). Approximate ranges: Natural Gas about 31 to 40 percent; Nuclear about 28 to 36 percent; Coal about 18 to 24 percent; Wind about 2 to 9 percent; Oil, Solar, Hydro and Other each roughly 0 to 5 percent."""
T["T2_caveat"] = ("exact coordinates of the unlabeled scatter points, exact number of points, exact hourly values in (b) and (c), "
                  "and exact series values are not recoverable; every number above for this figure is a visual estimate, "
                  "except axis ranges, tick values, legend entries, point labels and the 0.06 coefficient, which appear in the figure or caption.")
def _eq(tid, page, body):
    img = f"images/pdf_p0{page}_page.png"
    return f"<<<TRANSCRIPTION {tid} kind=equation pdf_page={page} image={img} produced_by=local_visual_inspection (not source text)>>> {body} <<<END TRANSCRIPTION {tid}>>>"
E1 = "rho_{s2,t} = ( SUM_k b_{k,t} x EWIF_k ) / ( SUM_k b_{k,t} )"
E2 = "Water_Operational = SUM_{t=1..T} e_t * [ rho_{s1,t} + theta_t * rho_{s2,t} ]"
E3 = "Water_Embodied = ( T * W ) / T0"
E4 = "Water_Total = SUM_{t=1..T} e_t * [ rho_{s1,t} + theta_t * rho_{s2,t} ] + ( T * W ) / T0"
EQUATIONS = [
 ("ρs2,t=\n\n∑kbk,t×EWIFk _ ∑kbk,t<sup>where b</sup>k,t<sup>denotes the</sup> amount",
  "ρs2,t = " + _eq("E1", 5, E1) + " where bk,t denotes the amount", "E1"),
 ("Water- Operational=∑t=1 Tet·[ρs1,t+θt·ρs2,t].", "Water-Operational = " + _eq("E2", 6, E2) + ".", "E2"),
 ("WaterEmbodied=<sup>T·W</sup> _ T0 By adding", "WaterEmbodied = " + _eq("E3", 6, E3) + " By adding", "E3"),
 ("WaterTotal=∑t=1 Tet·[ρs1,t+θt·ρs2,t] +<sup>T·W</sup> _ T0<sup>. In practice, to obtain a rough</sup> estimate",
  "WaterTotal = " + _eq("E4", 6, E4) + ". In practice, to obtain a rough estimate", "E4"),
]

# Kanbur et al. — Desalination-integrated data center cooling — reading notes

Reading steps for `kanbur_et_al_2020_desalination_integrated_data_center_cooling`, split at section headings and paragraph breaks into
roughly 200–500 words each. The split is mechanical: nothing here names a move or
says what a step means. Figure captions that interrupted a sentence are moved
after it. Equations and tables are marked with their crop image.

## Step 1 — Title, authors, and Summary (page 1, ~367 words)

> Multi-criteria thermoeconomic and thermodynamic assessments of the desalination-integrated two-phase liquid-immersion data center cooling system
>
> Baris Burak Kanbur<sup>1</sup> | Chenlong Wu<sup>1,2</sup> | Fei Duan<sup>1</sup>
>
> 1School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore, Singapore
>
> 2Energy Research Institute @ NTU, Nanyang Technological University, Singapore, Singapore
>
> Fei Duan, School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore, Singapore 639798. Email: feiduan@ntu.edu.sg
>
> Funding information
>
> Nanyang Technological University
>
> The waste heat management of the data center cooling systems has a significant share in the energy-efficient operations of the data centers. In this study, a new hybrid desalination-data center cooling system is proposed to reduce the cost drawback of the waste heat in the data center cooling operations. A two-phase liquid-immersion cooling unit is selected as the data center cooling method with the cooling load range of 0.7 to 1.5 kW. It is a promising solution thanks to the high heat flux removal performance but there is still a lack of research about waste heat management. The waste heat of the immersion cooling system is used to heat up the feed side of the desalination module. A direct contact membrane distillation system as preferred as the desalination module with the membrane area range of 5 to 75 cm<sup>2</sup> . The proposed hybrid system is investigated according to the thermodynamic, economic, and thermoeconomic aspects. The thermoeconomic assessment is done concerning the unique exergy-cost matrix of the original design. The maximum thermal and exergy efficiencies are found as 64.5% and 53.7%, respectively. The daily distilled water rate can reach 6.13 kg at the highest cooling load and membrane area. Compared to the stand-alone data center cooling operation, the hybrid system has higher capital and operation costs. The payback period is found 3.72 years that means the proposed system is economically feasible for real applications. Also, the levelized product cost of the hybrid design is calculated in the range of 2.69 to 5.33 SGD/h. In the multiobjective optimization study, the best trade-off point is decided at the cooling load of 1.1 kW whilst the membrane area varies between 5.12 and 5.19 cm<sup>2</sup> .
>
> K E Y W O R D S combined energy system, data center cooling, desalination, multiobjective optimization, thermodynamic analysis, thermoeconomic assessment

**Moves:**

**Claims:**

**Meaning:**

---

## Step 2 — 1 | INTRODUCTION (page 1, ~501 words)

> The increasing demand for the Information and Communication Technology (ICT) facilities make their uninterrupted operations more important compared to the past. Hence, the management of their housing spaces, which are called as Data Centers (DCs), have been becoming more crucial over time. The uninterrupted and stable operations of DCs bring a huge cost drawback from the point of energy consumption. In 2018, the global energy demand by DCs has reached 200 TWh.<sup>1</sup> The near-future projections state that the data centerrelated energy consumption will reach 70 TWh in 2020 only for the United States.<sup>2</sup> Compared to the standard office facilities, the energy demand by ICT equipment corresponds up to 100 times higher.<sup>3</sup> During the DC operation, the ICT equipment like network infrastructures and computing systems generate thermal energy at the chip, server, or rack level. The generated thermal energy must be released via cooling systems to achieve zero downtime and uninterrupted operations. That is, the main goal of the DC cooling process is to maintain the ICT equipment temperature at the desired levels. Rong et al<sup>4</sup> stated that the energy consumption of DC cooling systems shares roundly 40% of the total DC energy consumptions. Namely, the DC cooling systems have a pivotal role in the thermal management of DC systems. There are two DC cooling types which are air-cooled and liquid-cooled DC systems.<sup>5</sup> The air-cooled DC systems are the traditional systems to release the heat from DC units. The liquid-cooled DC systems have been recently being popular thanks to their high heat removal performance. Although the air-cooled and liquid-cooled DC systems have different configurations to cool down the DC unit, they generally use dry towers or economizers as common equipment to release the thermal energy to environment.<sup>6,7</sup> Alternatively, the released thermal energy from data centers systems can be used in waste heat recovery technologies such as combined heating and cooling,<sup>8</sup> district heating and hot water production,<sup>9</sup> and vapor compression.<sup>10</sup> Besides the above-mentioned waste heat recovery techniques, the seawater desalination by using the waste heat (steam) of data center cooling systems has also been proposed as an idea by Ebrahimi et al.<sup>11</sup> However, the modeling and performance assessment details were not given in that study. In fact, integration of the desalination process is a widely-proposed approach for different energy systems such as nuclear power plants,<sup>12</sup> marine energy and industry,<sup>13,14</sup> solar energy,<sup>15,16</sup> fuel cell and gas turbine<sup>17</sup> and thermoelectric coolers.<sup>18</sup> Those studies inferred that low-temperature energy systems can be efficiently combined with the desalination process. Thus, the combined solution of DC cooling and seawater desalination has also a strong potential for the real-scale systems. The generated thermal energy from the DC waste heat systems is able to provide a sufficient amount of energy for desalination units. In addition, the combined DC cooling and desalination has critical importance since it addresses both UN Sustainable Development Goals (SDGs) 6 (Clean Water and Sanitation) and 7 (Affordable and Clean Energy). Therefore, the current idea is in the scope of energywater nexus concept, which is compatible with the

**Moves:**

**Claims:**

**Meaning:**

---

## Step 3 — 1 | INTRODUCTION (continued) (page 1, ~585 words)

> Baris Burak Kanbur and Chenlong Wu share the first authorship.
>
> United Nations goals.<sup>19,20</sup> Up to now, there is no detailed understanding study for this concept so that it addresses a research gap to be filled. Furthermore, when the waste heat utilization of DC cooling systems is investigated in detail, it is seen that they have been usually based on the air-cooled systems. Nevertheless, the system-scale waste heat utilization studies on the liquid-cooled DC systems have not been widely-performed as far as we know. Hence, this brings another research gap that has a strong potential to develop more efficient waste heat utilization works.
>
> The liquid-cooled DC systems are able to remove higher heat flux compared to the air-cooled systems because the working liquids have higher heat removal performance; and therefore, they have been becoming more popular for the rapidly developing ICT facilities such as big data, cloud computing, smart cities/ manufacturing. The liquid-cooled DC systems can be categorized as direct and indirect DC cooling systems. Compared to the direct cooling systems, the indirect cooling systems are more established systems but they have also two major drawbacks which are (a) the leakage potential during the liquid circulation in a piping system and (b) the specific system layout sizing according to the required DC cooling load. The direct cooling systems overcome these challenges; (a) they directly contact the ICT equipment surface by means of the dielectric liquids that mean no liquid piping requirement at server or rack level, (b) they are very flexible systems which can be modified for different DC cooling loads. The direct cooling systems are the methods of jet impingement, spray cooling, and two-phase liquid-immersion cooling. In principle, these methods can be set up for an independent DC cooling operation or combined with the conventional air-cooled techniques. Amongst others, the twophase liquid-immersion cooling systems provide a more uniform temperature distribution on the ICT equipment surface thanks to its two-phase heat transfer (latent heat transfer mechanism). More details on the liquid-cooled DC systems can be found in References 21–24. Even though the direct cooling systems are less complex and the two-phase liquid-immersion cooling systems are more advantageous, they still do not have wide-spread system-scale studies. Recently, some ICT companies like Submer Inc., GIGABYTE, 3M, and FUJITSU have been conducting system-scale studies on the two-phase liquidimmersion cooling studies, but there is still a lack of thermal management and economic assessment research that brings an important gap from the academic perspective. To fill this gap, we have recently started to work on the system-scale performance assessments of the two-phase liquid-immersion DC cooling systems. In our first study, we developed a real-scale experimental setup and investigated the transient performance of the system up to 21 kW.<sup>25</sup> Since the results achieved satisfying steady performance in real conditions, we have developed a mathematical model for the DC cooling unit and combined the system with a polymer electrolyte membrane fuel cell unit to generate electricity with the waste heat of the DC cooling unit.<sup>26</sup> That study inferred that the lowcarbon electricity generation can be obtained with the DC cooling load of nearly 6 kW. However, as mentioned above, the two-phase liquid-immersion DC cooling systems can be flexible with respect to the cooling load. For the DC cooling loads below 6 kW, the waste heat utilization may not be efficient for low-carbon electricity generation or other well-known thermal processes. Therefore, for lower DC cooling loads, there is a research gap for more efficient and economic operations of the two-phase liquid-immersion DC cooling systems.

**Moves:**

**Claims:**

**Meaning:**

---

## Step 4 — 1 | INTRODUCTION (continued) (page 3, ~212 words)

> The study points out the highlighted research gap and proposes a novel hybrid system solution. The main original contributions are listed as follows: (a) the proposed system has not been investigated before. It utilizes the waste heat of the data center cooling system in the direct contact membrane distillation (DCMD) module. In this way, clean water production can be achieved. (b) it is the first time of the two-phase liquid-immersion cooling system for the waste heat utilization via desalination purposes. This brings a new alternative to the data center cooling systems, especially for low DC cooling loads. (c) A unique exergy-cost matrix is built since the proposed hybrid system is new and has not been investigated before. Besides the thermoeconomic model, the hybrid design is assessed according to the economic and thermodynamic aspects. The generated exergy-cost matrix can be useful in the waste heat utilization studies of future two-phase liquid-immersion cooling systems. (d) The fourth and last contribution is the multiobjective optimization study. The minimization of the distilled water cost and system product cost and the maximization of exergy efficiency are the multiple objectives. The design constraints are the DC cooling load and the membrane application area with the ranges of 0.7 to 1.5 kW, and 5 to 75 cm<sup>2</sup> , respectively.

**Moves:**

**Claims:**

**Meaning:**

---

## Step 5 — 2 | SYSTEM DESCRIPTION (page 3, ~530 words)

> The simplified schematic of the new proposed combined system is shown in Figure 1. Stream 1 denotes the seawater with the salinity of 35 g/L (TDS of standard seawater<sup>27</sup> ) and temperature of 302.75 K (Singapore seawater temperature<sup>28</sup> ) at 1 atm. It enters the two-phase liquidimmersion DC cooling unit that has a pump and a server tank. The seawater inlet to the server tank is denoted by stream 2. The pump is assumed as EB120 pump by Euroflo while the server tank is a customized server tank that can operate the liquid-immersion cooling operations up to 2 kW released heat rate from the servers. The server tank is filled with NOVEC 7100 dielectric liquid with the boiling temperature of 61<sup>�</sup> C. The servers are submerged in the dielectric liquid bath and the generated energy from the servers increases the liquid bath temperature up to boiling temperature value. The imposed power rate by the servers is assumed constant that can allow steadystate thermodynamic assessments.<sup>29</sup> The vapor bubbles in the liquid bath start to rise at the top of the tank where the condenser pipes, which circulates coolant inside, are located. Since the circulated coolant temperature is lower than the boiling temperature, the vapor bubbles condense on the pipe surface. Then they drop into the liquid bath. During this process, the coolant temperature increases due to the heat transfer from the vapor bubbles. The proposed two-phase liquid-immersion DC cooling setup was experimentally operated and verified in our previous work.<sup>25</sup> In this study, we circulate the seawater as a coolant so that it is heated up in the DC tank. The seawater outlet temperature, T3, increases before entering the DCMD module. At this point, a temperature limit arises as a design criterion. As the nature of heat transfer and thermodynamics, the seawater temperature (stream 3) cannot be higher than the boiling temperature of the dielectric liquid bath, 61<sup>�</sup> C. From the point of engineering, stream 3 temperature must be lower than 61<sup>�</sup> C; therefore, we determine the temperature difference limit as 3 K between the boiling temperature of dielectric liquid and the seawater 3 temperature. Then, stream 3 enters the feed side of the DCMD module that is the oldest technique of membrane distillation with a membrane interface excluding the air gap or conductive material interface.<sup>30</sup> On the another side of the DCMD module, the permeate flow enters the module as stream 6 after pumping via another circulation pump that has inlet stream (stream 5) with the temperature of 293.15 K. In the module, due to the temperature difference between the feed and permeate sides, the vapor pressure at feed and permeate sides becomes different than each other; in this way, the mass and heat transport occurs through the hydrophobic membrane that blocks the liquid transport whilst allow for the vapor transfer. By means of the transport phenomena, the mass flow rates of inlet streams are not equal to the mass flow rates of outlet streams. For the feed side, the mass flow rate of seawater outlet, stream 4, is lower while the mass flow rate of permeate outlet, stream 7, has higher mass flow rate than the inlet stream (stream 6).

**Moves:**

**Claims:**

**Meaning:**

---

## Step 6 — 2 | SYSTEM DESCRIPTION (continued) (page 3, ~245 words)

> The study has some system assumptions and inlet parameters. The system is assumed to be operated under the steady-state conditions and membrane fouling is neglected. The DCMD module and server tank are assumed well-insulated without any heat loss rate. The piping of the hybrid system is also considered as wellinsulated since the previous experimental data center cooling study<sup>25</sup> showed that the heat loss through the pipe is very small thanks to the insulated pipes and the low temperature difference between the operating liquid temperature and the ambient temperature. The released heat from the servers is assumed in the range of 0.7 and 1.5 kW. The heat and mass transfer characteristics of the DCMD module is withdrawn from Reference 31. The velocity and hydraulic diameter are determined as 1.85 m/s and 0.003 m for the feed side, respectively, while the permeate side has the inlet velocity of 2.92 m/s with the same hydraulic diameter value. The corrosion and salt deposition in the water pipe is neglected in performance calculations and for pipeline damage. The PVDF membrane with the thickness, thermal conductivity, porosity, and pore size values of 126 μm, 0.41 W/mK, 0.75, and 0.22 μm are also withdrawn from Reference 31. The membrane area is selected in the range of 5 to 75 cm<sup>2</sup> . The reference state temperature and pressure are 293.15 K and 1 atm. Following the withdrawn DCMD data from Reference 31, the developed DCMD mathematical model is also validated with Reference 31.
>
> *[equation E1, page 4 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E1_p04.png)]*

**Moves:**

**Claims:**

**Meaning:**

---

## Step 7 — 3 | MODELING and 3.1 | Thermodynamic model (page 4, ~480 words)

> The combined system modeling has five sections which are the thermodynamic model, thermodynamic model validation, economic model, thermoeconomic model, and the multiobjective optimization procedure. The entire flow of the methodology can be seen in Figure 2.
>
> FIGURE 1 The schematic of the proposed combined liquidcooling data center and direct contact membrane distillation system [Colour figure can be viewed at wileyonlinelibrary.com]
>
> The proposed system is investigated from the perspectives of energetic and exergetic assessments. The energy model is based on enthalpy-related thermodynamic assessment. Seawater flow at the feed side and the water at the permeate side are two different fluids of the DCMD unit. The specific enthalpy of water at stream i, hwi , can be read from different thermophysical property sources, but we use the correlations by Sharqawy et al<sup>32</sup> in Equation (1), where ti is the temperature of stream i with the Celsius unit. The unit of hwi is J/kg in this correlation. After calculating the specific enthalpy of water, the water enthalpy rate of stream i, Hwi , is calculated by multiplying the mass flow rate of water at stream i, m_ wi , and hwi . The m_ wi is obtained from the volume flow rate, υ_ , which can be found by using the hydraulic diameter, dh, and flow velocity, v, at both feed and permeate sides. After that, υ_ is multiplied by the density of water at stream i, ρwi , which is defined in Equation (2),
>
> FIGURE 2 The solution algorithm of the proposed combined system [Colour figure can be viewed at wileyonlinelibrary.com]
>
> *[equation E2, page 5 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E2_p05.png)]*
>
> In the DCMD module, the enthalpy rates of streams 5 to 7 can be found with Equations (1) and (2). However, for streams 1 to 4, the thermophysical properties of seawater are required. The specific enthalpy of seawater at stream i, hswi is given in Equation (3), where S is the salinity of seawater. The coefficients Ai − Ci are explained in Appendix A. In addition, the correlation for the density of seawater at stream i, ρswi is given in Equation (4),
>
> *[equation E3, page 5 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E3_p05.png)]*
>
> where F1i is 0.5. The coefficients F2i − F4i and A1i −A4i are presented in Appendix B. Similar to the water enthalpy rate, the seawater enthalpy rate at stream i, Hswi , can be obtained by multiplying the mass flow rate of seawater at stream i, m_ swi , and hswi . Following Equations (1) to (4), H1 and H5 can be found at the feed side and permeate side, respectively. The values of H1 and H5 allow us calculating H2 and H6 by using the pump work rate. Equations (5) and (6) present the calculation of H2 and H6, respectively, where W<sup>_</sup> fp and W<sup>_</sup> pp are the power rates of the feed and permeate pumps, respectively. The calculation of H2 makes the possible to write an energy balance for DC server tank as shown in Equation (7),

**Moves:**

**Claims:**

**Meaning:**

---

## Step 8 — 3.1 | Thermodynamic model (continued) (page 5, ~471 words)

> The enthalpy is the function of temperature so that T3 can be found. Then, the thermal model of the DCMD can be created. Since the feed side has higher temperature, heat transfer occurs from the feed side to the permeate side through the membrane. To calculate the heat transfer rate, the heat flux between the feed flow and membrane (q<sup>00</sup> f<sup>),insidethemembrane(q</sup> m<sup>00),andbetweenthe</sup> membrane and permeate flow (q<sup>00</sup> p<sup>)mustbedefined.</sup> Equation (8) presents the q<sup>00</sup> f<sup>,</sup> where αf is the convective heat transfer coefficient of feed flow whereas Tf is the feed flow temperature, which is equal to T3, and Tf, m is the temperature of the membrane surface at feed flow side. Similarly, q<sup>00</sup> p<sup>canbedefined</sup> between the permeate side of the membrane and the permeate flow as shown in Equation (9),
>
> *[equation E4, page 5 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E4_p05.png)]*
>
> in which αp is the convective heat transfer coefficient of permeate flow whereas Tp is the permeate flow temperature, which is equal to T6, and Tp, m is the temperature of the membrane surface at permeate flow side. Due to the direction of heat and mass transfer, we can define the temperature limits as Tf > Tf, m > Tp, m > Tp. Hereby, the convective heat transfer coefficients can be calculated by using the channel characteristics and fluid properties of the feed and permeate sides. Equation (10) explains the convective heat transfer coefficient, α, according to the channel characteristics and fluid properties,
>
> *[equation E5, page 5 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E5_p05.png)]*
>
> where k is the thermal conductivity of fluid and dh is the hydraulic diameter. The dimensionless Nusselt number,
>
> Nu, can be explained by the Dittus and Boelter correlation as shown in Equation (11),<sup>31</sup> in which L is the DCMD module length, Re and Pr dimensionless Reynolds and Prandtl number, respectively. Besides the terms of q<sup>00</sup> p<sup>andq00</sup> f<sup>,theheatfluxinsidethe</sup> membrane, q<sup>00</sup> m<sup>,shouldbemodeledtocompletethe</sup> DCMD model since the heat flux inside the membrane is the middle step between q<sup>00</sup> f<sup>andq</sup> p<sup>00.Therearetwoheat</sup> transfer mechanisms in the membrane which are the latent heat of evaporation and the heat conduction. Equation (12) presents the q<sup>00</sup> m<sup>,</sup>
>
> *[equation E6, page 6 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E6_p06.png)]*
>
> where J is the mass flux through the membrane module, Δhfg is the specific enthalpy of vaporization, km is the thermal conductivity of membrane, and δm is the thickness of membrane. To calculate the Δhfg, the experimental correlation was withdrawn from Reference 31. However, the physical model of the Δhfg can be built by means of the non-equilibrium thermodynamic fundamentals and the Clausius-Clapeyron equation as explained in detail by Luo and Lior.<sup>33</sup> The first term on the right side of Equation (12), J � Δhfg, denotes the heat flux via vapor (latent heat of evaporation) whilst the second term, (km/δm) � (Tf, m − Tp, m), shows the heat flux via conductive heat transfer. The mass flux rate, J, is directly related to the transferred mass from the feed side to the permeate side as shown in Equation (13),
>
> *[equation E7, page 6 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E7_p06.png)]*

**Moves:**

**Claims:**

**Meaning:**

---

## Step 9 — 3.1 | Thermodynamic model (continued) (page 6, ~424 words)

> where Am is the membrane area in the DCMD module. There are also different ways to calculate the mass flux rate in the DCMD module such as (a) multiplying the membrane permeability with the vapor pressure difference between the feed and permeate sides of the membrane surface and (b) using the non-equilibrium thermodynamic fundamentals (eg, vapor free path) and membrane characteristics (eg, porosity, average pore size diameter, average membrane temperature, membrane thickness). However, the membrane characteristics are determined via experimental measurements that may result in additional uncertainties.<sup>34</sup> More details about these methods can be found in Reference 33. Compared to the foregoing alternatives, the use of mass flow rates is an easier way to calculate the mass flux rate especially for the experimental setups. In the module, the heat loss through the DCMD module surface is neglected; hence, the energy balance for the DCMD module can be written as given in Equation (14),
>
> The solution procedure between Equations (8) to (14) requires an iterative study since the defined parameters are depend on the temperature values where T3 and T6 are known and Tf, m and Tp, m are unknown. As the initial step, Tf, m is estimated; and then, the iterative study is completed when Equation (14) is obtained. After that, the exact mass flux, transferred mass, and all the temperature values can be seen. In the iteration loop (Equations (8) to (14)), the Prandtl number (Pr) in Equation (11) is calculated for the feed and permeate sides separately since feed and permeate temperatures are different than one another. For the feed side, the Pr is calculated at the temperature value of (Tf + Tf, m)/2 while it is calculated at the temperature value of (Tp + Tp, m)/2 for the permeate side.<sup>31</sup> Once the iteration study is accurately done, the final Pr value is calculated according to the iterated Tf, Tf, m, Tp, m and Tp values. It must be noted that the use of average temperature to calculate the Pr at both feed and permeate sides is a reasonable solution step for the small-scale DCMD setups. However, it must be replaced by the dynamic observation of temperature gradients between Tf and Tf, m and Tp and Tp, m for the large-scale commercial DCMD systems since the temperature changes may not be linear between the feed/permeate and membrane surface. The overall energy balance is written for the DCMD module to calculate the temperature, enthalpy, and entropy of streams 4 and 7. The energy balance of the DCMD module is written in Equation (15),

**Moves:**

**Claims:**

**Meaning:**

---

## Step 10 — 3.1 | Thermodynamic model (continued) (page 6, ~494 words)

> More details on the DCMD modeling and energy balance can be found in the study by Luo and Lior.<sup>33</sup> Furthermore, the obtained temperature values also allow calculating the entropy values for the exergy assessments. Similar to the enthalpy calculations, the water and seawater have different correlations for the entropy as given in Equations (16) and (17), respectively,<sup>32</sup> where Asi −Csi are coefficients and explained in Appendix C. Exergy assessments consider the second-law related destruction and loss terms that are not able to be obtained via energy assessments. Similar to the energy analysis, each stream has a specific exergy, e, as written in Equation (18),<sup>35</sup> in which h0 and s0 are the specific enthalpy and entropy at reference state. The multiplication of ei and m_ i gives the exergy rate of stream i, Ei. It must be noted that the specific exergy can also include the chemical exergy terms but they are not considered in this study since there is no change in the chemical components of the streams. More details on the exergy assessments can be found in References 36 and 37. After calculating the exergy rates of the streams, the exergy balance equation can be defined as shown in Equation (19), where E<sup>_</sup> F , E<sup>_</sup> P, E<sup>_</sup> D, E<sup>_</sup> L, E<sup>_</sup> G and are the exergy rates of fuel, product, destruction, loss, and gain, respectively. The E<sup>_</sup> L term is related to the heat loss so that it can be neglected since zero heat loss is assumed in the combined system. However, the E<sup>_</sup> G term must be taken into account due to the fact that the combined system gains thermal energy from the servers, Q<sup>_</sup> DC.
>
> The energetic and exergetic assessments are done by using performance criteria. The combined system has two sub-systems which are the data center cooling system and the DCMD module. The thermodynamic performance of the data center cooling system is analyzed via the coefficient of performance, COP, which simply means the ratio of the desired energy removal rate from the system to the consumed energy rate, as defined in Equation (20), total energy input. In the membrane distillation systems, the maximum GOR value is desired. On the other hand, PR defines the ratio of produced clean water rate to the inlet feed water rate. Both GOR and PR are written in Equations (22) and (23), respectively,
>
> For the exergetic assessments, the exergy efficiency, ε, is the most-known assessment criterion. The exergy assessments can also be used in sustainability assessments. Rosen et al<sup>38</sup> stated the sustainability performance as the ratio of the fuel exergy rate to the destruction exergy rate, which was called as the sustainability index, SI. Both ε and SI are presented in Equations (24) and (25), respectively,
>
> *[equation E8, page 7 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E8_p07.png)]*
>
> Hereby, it can be said that the increment in fuel exergy rate via better utilization grows the SI of the combined system. Also, the decrement in the exergy destruction rate via better design considerations achieves higher SI trends.

**Moves:**

**Claims:**

**Meaning:**

---

## Step 11 — 3.2 | Thermodynamic model validation (page 7, ~373 words)

> where Q<sup>_</sup> DC is the released heat rate from the data center tank. For the thermodynamic performance of the DCMD module, the thermal efficiency is written in Equation (21),
>
> Besides the thermal efficiency, there are two different energy performance criteria which are the gain output ratio, GOR, and performance ratio, PR. GOR represents the ratio of heat transfer rate via vapor to the total heat input to see the share of the vapor-related heat rate in the
>
> Before applying the built energy and exergy models to the proposed combined system, the validation of the DCMD module is done by comparing the results with the results of Reference 31. In that study, the DCMD performance was investigated at four different feed water (seawater) temperatures which were between 40 and 70<sup>�</sup> C with 10<sup>�</sup> C intervals while the permeate flow temperature was 20<sup>�</sup> C. For comparison purposes, the data center unit was not considered and the present DCMD module is analyzed with the same temperature and flow rates with Reference 31. The absolute value of the relative difference is calculated between the current DCMD model and the results by Reference 31. Table 1 presents that the percentage of the obtained difference which are less than 1% at the temperature values of 40<sup>�</sup> C, 60<sup>�</sup> C, and 70<sup>�</sup> C while the model comparison at 50<sup>�</sup> C has less than 1.5% difference. The obtained results clearly infer that the current mathematical model of the DCMD module is in a very good agreement with the reference study.
>
> Besides, the thermodynamic validation of the twophase liquid-immersion DC cooling system was achieved via our former studies. In our experimental study, we have already provided that the system-scale two-phase liquid-immersion DC cooling unit can be operated at steady conditions up to the Q<sup>_</sup> DC of 21 kW.<sup>25</sup> On the other hand, the mathematical model of the data center cooling unit was developed in our previous modeling study.<sup>26</sup> More details on the experimental thermodynamic operation and mathematical modeling can be found in References 25 and 26. It is worth to remind that the validation of the proposed hybrid model is currently not possible since the proposed system is firstly presented in this paper; but, further studies will focus on their small-scale demonstration.

**Moves:**

**Claims:**

**Meaning:**

---

## Step 12 — 3.3 | Economic model (page 8, ~658 words)

> The economic performance assessment is done with the payback period calculation. Payback period, PP, simply means the return of the investment over time. The PP calculation of the proposed hybrid system is done by referring to the stand-alone two-phase liquid-immersion DC cooling unit. In the stand-alone system, the DC cooling unit is assumed with the streams 1 to 3 in Figure 1. That is, the stand-alone DC cooling system has a seawater inlet with the feed pump power; and then, it leaves the DC cooling tank as stream 3. Compared to the proposed hybrid design, the stand-alone system does not consist of the permeate pump and the DCMD module. Therefore, its capital investment cost and future cost (eg, electricity consumption, operation and maintenance cost, replacement cost) are lower than the hybrid system costs. However, even though the hybrid system has higher capital investment and future cost terms, the distilled water is the product of the DCMD module, and the economic impact of the distilled water can be used to understand whether the proposed hybrid system is economically more feasible than the stand-alone DC cooling operation or not. The payback period is explained in Equation (26), where TCI is the total capital investment, Cw is the annual cost of the distilled water generated by the system, Chyb is the total annual cost of the hybrid system, and Cs − alone is the total annual cost of the stand-alone system. TCI consists of fixed capital investment and other outlays.<sup>36</sup> The fixed capital investment includes the direct costs (eg, purchased equipment cost, installation of purchased equipment, piping, instrumentation and control, electrical equipment, land, and structural costs) and the indirect costs (engineering and supervision cost, contingencies, etc.). On the other hand, the other outlays mean the startup cost, working capital, and R&D costs. In fact, TCI is a very wide definition so that it is very difficult to calculate it for the energy systems, especially for the newproposed energy systems like the current idea. To deal with this complexity, Bejan et al<sup>36</sup> presented a simple formula that gives a direct relation between the TCI and the purchased equipment cost, PEC, as shown in Equation (27), where PEC is the purchased equipment cost of the system equipment that is presented in Table 2 according to our experimental setup study<sup>25</sup> and the study by Swaminathan et al<sup>39</sup> for the DC cooling and DCMD modules, respectively. It must be noted that the coefficient of 6.32 is a cost estimation approach for TCI by using the PEC values. There are also other cost estimation techniques or coefficients, but we prefer to use the coefficient of 6.32 from Bejan et al<sup>36</sup> since it is a well-known and widely-preferred coefficient. It is worth mentioning that the given payback period definition is a simple definition for the economic assessment. Since both hybrid and stand-alone systems have the same system lifetime and interest rate values, the basic payback period definition seems sufficient for a comparison purpose. For more detailed economic assessments, the life cycle costing-based economic analyses (eg, payback period calculation via cumulative present worth trends, or return on investment analyses via annual costs) can be preferred. Cw is calculated by the product of distilled water rate with the unit water cost of Singapore cw, as shown in Equation (31), where cw = 2.74 m<sup>3</sup> /h,<sup>40</sup> and m_ dw = m_ 3 −m_ 4 = m_ 7 −m_ 6 . Chyb is the summation of the annual electricity cost of the hybrid system, Celhyb , annual operation and maintenance cost of the hybrid system, COMhyb , and the annual replacement cost of the hybrid system, CRChyb . The COMhyb is assumed 1.092% of the PEChyb. This assumed value is widely-used in energy systems<sup>41</sup> and we previously used in our previous economic and thermoeconomic assessments.<sup>42</sup> The CRChyb term is directly related to the DCMD module, because the DC cooling unit has nothing crucial for the replacement cost and the required replacement

**Moves:**

**Claims:**

**Meaning:**

---

## Step 13 — 3.3 | Economic model (continued) (page 8, ~403 words)

> TABLE 1 Validation of the solution algorithm with Reference 31
>
> ||U(W/m<sup>2</sup>K|)||q<sup>T </sup>(W/m<sup>2</sup>|K)||q<sup>T </sup>(W/m<sup>2</sup>|K)||
> |---|---|---|---|---|---|---|---|---|---|
> |Tfeed|Current||Relative|Current||Relative|Current||Relative|
> |(T3)|study|Ref.|difference (%)|study|Ref.|difference (%)|study|Ref.|difference (%)|
> |40|524.75|524.88|0.025|10 495.00|10 498.00|0.029|4532.90|4496.00|0.821|
> |50|692.81|701.01|1.169|20 784.00|21 030.00|1.170|12 098.00|12 252.00|1.257|
> |60|844.81|841.32|0.415|33 792.00|33 853.00|0.180|22 278.00|22 159.00|0.537|
> |70|980.75|985.34|0.466|49 037.00|49 267.00|0.467|35 073.00|35 147.00|0.211|
>
> *[table T1, page 9 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/T1_p09.png)]*
>
> costs can be considered as the part of COMhyb . However, the DCMD module consists of the membrane which requires periodic replacement and this results in high replacement cost values; hence, the replacement cost term should be considered separately from the classical operation&maintenance cost term. Al-Obaidani et al<sup>27</sup> defines the CRCm as 15% of the PECm in the membrane distillation operations; hence, we used the same ratio for the replacement costs of the DCMD module. While the COMhyb and CRChyb can be defined with PEC values, Celhyb is calculated by the product of the unit electricity cost, cel, and the total consumed electricity by the feed and permeate pumps, as defined in Equation (32),
>
> TABLE 2 Purchased equipment cost of the hybrid system equipment
>
> |Component|Price|
> |---|---|
> |DC cooling tank|1775.00 SGD/kW-DC|
> ||cooling load<sup>25 a b</sup>|
> |Feed and permeate pumps|950.00 SGD<sup>25 b</sup>|
> |DCMD module|140.00 SGD/m<sup>239 c</sup>|
>
> *[table T2, page 9 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/T2_p09.png)]*
>
> aIncludes the tank, condenser pipe, and dielectric liquid prices. bPrices are collected from the cost of our experimental setup equipment. cConverted from the USD currency to the SGD currency.
>
> an acceptable value regarding the previous economic analyses of the DC cooling<sup>44,45</sup> and DCMD module.<sup>27</sup>
>
> where cel = 0.2552 SGD/kWh.<sup>43</sup> In Cs − alone calculations, COMs −alone is the 1.092% of the PECs − alone and the CRCs −alone is assumed zero since the stand-alone system only consists of the DC cooling unit that does not have a crucial replacement cost differently from the COMs −alone term as mentioned above. The Cels − alone is obtained by the product of the cel and the feedwater pump since the permeate pump is not a part of the stand-alone DC cooling operation. The Cels − alone is defined in Equation (33),
>
> In the economic analysis, the system lifetime is assumed 20 years; therefore, the PP will be economically infeasible if it will be calculated for more than 20 years. It is worth mentioning that the assumed lifetime is not the lifetime of the operated servers (ICT equipment) in the cooling tank, because the ICT equipment can be replaced multiple times according to its performance. The system lifetime directly means the lifetime of the DC cooling and DCMD equipment. The n value of 20 years is

**Moves:**

**Claims:**

**Meaning:**

---

## Step 14 — 3.4 | Thermoeconomic model (page 9, ~475 words)

> Thermoeconomic model combines both thermodynamic and economic parameters to provide a single methodology instead of two different aspects. In the current work, the exergetic parameters are used in the thermoeconomic model and the exergy-cost matrix, which is a unique cost matrix for each original energy system, is built with respect to the economic and exergetic parameters.<sup>46</sup> A unit cost value, c, is defined for each system stream. In the hybrid system, the unit cost of stream 1, c1, is assumed zero since the seawater does not have a cost at atmospheric conditions. However, the inlet water stream to the system, stream 5, has the unit water cost of Singapore, cw = c5 = 2.74 m<sup>3</sup> /h, from the economic analysis. Also, the unit costs of the electricity inputs for the feed and permeate pumps are equal to the electricity price in the economic analysis, cel = c8 = c9 = 0.2552 SGD/kWh. Although we are able to define the unit costs of the inlet streams with electricity and/or water prices, the unit costs of the internal streams (eg, streams 2-4,6,7) are not known. To calculate the unit costs of the internal streams, the exergy cost matrix is built with the thermoeconomic balance equation, which is shown in Equation (31), where C<sup>_</sup> p and C<sup>_</sup> f are the levelized product and fuel costs of the system component, respectively; Z<sup>_</sup> k is the levelized component cost of component k. The levelized cost, C<sup>_</sup> , is obtained by multiplying the unit cost of the stream, c, with the exergy rate, E<sup>_</sup> . The product and fuel cost terms depend on the inlet and outlet streams of the system component. The levelized component cost is calculated by considering the purchased equipment and future cost terms with the capital recovery factor and annual operating time (hours) as given in Equation (32), where CO & M is the operation and maintenance cost that is equal to 1.092% of PEC,<sup>42</sup> τ is the annual operating time with 8000 hours, and CRF is the capital recovery factor which is explained in Equation (33),
>
> *[equation E9, page 10 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E9_p10.png)]*
>
> where i and n are the interest rate and system lifetime with 1.7% and 20 years, respectively. The exergy cost matrix consists of relationships between the balance equations of system components; therefore the unit costs of the internal streams can be calculated. Table 3 presents the thermoeconomic balance equations for all system components, and the exergy-cost matrix of the hybrid system is given in Equation (34), where u1 − 4 are unknown unit cost parameters and represent internal streams of the hybrid system as projected in Table 3. In thermoeconomic assessments, the main goal is to reach the minimum C<sup>_</sup> p value for the overall system.<sup>36</sup> Besides the minimum C<sup>_</sup> p goal, the minimum levelized cost of the produced distilled water, C<sup>_</sup> dw, can be specifically aimed in this study.

**Moves:**

**Claims:**

**Meaning:**

---

## Step 15 — 3.5 | Multiobjective optimization procedure (page 10, ~543 words)

> The hybrid system can be investigated from the viewpoints of thermodynamics (both energetic and exergetic), economics, and thermoeconomics. However, their performance assessment criteria and relevant performance trends are different than one another; therefore, the multi-criteria decision-making step is required for the proposed hybrid design. For this purpose, the multiobjective optimization procedure is developed in this study and the best trade-off point is found with the genetic algorithm tool in the MATLAB environment. As illustrated in Figure 2, the multiobjective optimization starts when the thermodynamic, economic, and thermoeconoic results are obtained. In the current study, we define two different coupled-objectives which are (a) ε −C<sup>_</sup> p, and (b) ε− C<sup>_</sup> dw, respectively. The first coupledobjectives are two of the most preferred objective functions in the multiobjective optimization studies of energy systems,<sup>47</sup> and the multiobjective optimization simply aims to find the best trade-off point according to the maximum exergetic efficiency and the minimum levelized product cost. In addition, we also perform the second coupled-objectives apart from the first coupled-objectives, because the proposed system is not only an original design from the viewpoints of the combined energy systems and the data center waste heat utilization, but also novel with respect to the energy-water nexus perspective. Therefore, the minimization of the distilled water cost is coupled with the maximum exergy efficiency goal; and then, the trends between these two coupled-objective functions are investigated. The multiobjective optimization procedure is explained in Equation (35),
>
> *[equation E10, page 10 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E10_p10.png)]*
>
> |System||Thermoeconomic auxiliary|
> |---|---|---|
> |components|Balance equations|equations|
> |Feed pump|_C1+cel�_Wfp+ _Zfp= _C2|c1= 0,c2=u1|
> |DC-tank|_C2+cdc�_EG+ _ZDC-Tank= _C3|c2=c3=u1,cdc=u2|
> |Membrane|_C3+ _C6+ _ZDCMD= _C4+ _C7+ _Cdw|c6=c7=u3,cdw=u4|
> |Permeate pump|_C5+cel�_Wpp+ _Zpp= _C6|c3=u3|
>
> *[table T3, page 10 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/T3_p10.png)]*
>
> TABLE 3 Thermoeconomic balance equations of the hybrid system
>
> MOF1 = max ε½ � and min�C<sup>_</sup> p� 0:7 kW ≤ QDC ≤ 1:5 kW MOF2 = max ε½ � and min�C<sup>_</sup> dw� subject to 5 cm<sup>2</sup> ≤ Am ≤ 75 cm<sup>2:</sup> ð35Þ
>
> *[equation E11, page 11 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E11_p11.png)]*
>
> Once the performance trends of ε, C<sup>_</sup> p , and C<sup>_</sup> dw are collected in the MATLAB environment, the genetic algorithm-based optimization tool is used to conduct multiobjective optimization. The optimization results present the Pareto frontier plots of the multiobjective functions (MOFs). The Pareto frontier plot shows the optimal points of the multiobjective optimization problem, and the best trade-off point is selected according to the design criteria by the decision-maker which can be a person or an algorithm. To decide the best trade-off point, there are different weighting approaches such as weighted-sum and weighted-product.<sup>47</sup> In this study, the weighted-sum approach is preferred for determining the best trade-off point. For weighting, the utopia and the pseudo-nadir points of the Pareto frontier plot are used in the normalization step of the objective functions. Equation (36) shows the normalization formula for the objective function,
>
> *[equation E12, page 11 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E12_p11.png)]*
>
> where f<sup>*</sup> is the normalized value of the objective function in the Pareto frontier plot, f is the real value of the objective function, f<sup>U</sup> is the utopia point (the ideal case of the multiobjective optimization problem), and f<sup>PN</sup> is the pseudo-nadir point (the worst case of the multiobjective optimization problem between the anchor points of the Pareto frontier plot). After normalizing the objective functions, the weighted-sum, WS, can be defined with Equation (37), where ω is the weighting percentage of the objective functions. In the current work, the same weighting percentages (50%) are applied to the WS calculations.
>
> *[equation E13, page 11 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E13_p11.png)]*

**Moves:**

**Claims:**

**Meaning:**

---

## Step 16 — 4 | RESULTS AND DISCUSSION (page 11, ~421 words)

> The stand-alone thermodynamic performances of the data center cooling and the DCMD module are presented in Figures 3A,B, respectively. In Figure 3A, it is seen that T3 increases from 316.68 to 330.92 K when Q<sup>_</sup> DC rises from 0.7 to 1.5 kW. That is, the increment of 0.8 kW in servers increases T3 value roundly by 4.5%. Since the DCMD performance is directly affected by T3, it is stated that the impact of Q<sup>_</sup> DC on the DCMD performance is crucial. In parallel to the T3 increment, the COP trends of the maximum Q<sup>_</sup> DC are 2.15 times as high as the minimum Q<sup>_</sup> DC . Figure 3B shows the DCMD performance from the points of heat and mass fluxes. The maximum q00 and J values are found 30.68 kW/m<sup>2</sup> and 34.05 kg/m<sup>2</sup> h at the highest Q_ DC values, 1.5 kW. From 1.5 to 0.7 kW, q00 and J drop by 55.1 and 64.9%, respectively.
>
> FIGURE 3 Stand-alone evaluations of A, liquid cooling data center system and B, direct contact membrane distillation system according to the released heat rate from the system servers [Colour figure can be viewed at wileyonlinelibrary.com]
>
> The performance trends of the DCMD module due to the different released heat rate from the data center cooling system result in drastic changes in the product water rate. Figure 4 projects the produced water rate at different membrane area and Q<sup>_</sup> DC values. When Q<sup>_</sup> DC decreases from 1.5 to 0.7 kW, the produced water rate drops by nearly 65%, which is a significant decrement and shows the impact of the data center cooling rate on the combined system performance. On the other hand, when the applied membrane area is investigated between 5 and 75 cm<sup>2</sup> , it is observed that the produced water rate with 5 cm<sup>2</sup> is 93.3% smaller than the produced water rate with 75 cm<sup>2</sup> . This outcome infers that the applied membrane area has a pivotal role in the produced water rate trends. On the other hand, the increment in the membrane area brings high future cost terms (eg, operation, maintenance, replacement, energy) so that the trade-off study (eg, multiobjective optimization) will consider the DCMD module cost that is shown in Table 2. The data center cooling system is an uninterrupted operation with 24 hours in a day; hence, the daily produced water rate range is obtained between 0.14 and 6.13 kg according to the applied membrane area.
>
> FIGURE 4 Produced water rate from the combined system [Colour figure can be viewed at wileyonlinelibrary.com]

**Moves:**

**Claims:**

**Meaning:**

---

## Step 17 — 4 | RESULTS AND DISCUSSION (continued) (page 12, ~499 words)

> The energy and exergy efficiencies are illustrated in Figures 5A,B, respectively. The membrane thermal efficiency is independent of the membrane area, it only depends on the ratio of the heat flux via vapor to the total heat flux, as defined in Equation (21). The η trends deduce that the minimum thermal efficiency is calculated as 50.1% while the maximum is found as 64.5%. That is, the efficiency increases by 28.8% from the lowest Q<sup>_</sup> DC to the highest Q<sup>_</sup> DC . The ε trends are affected by both membrane area and Q<sup>_</sup> DC due to the differences in exergy destruction rates. From 0.7 to 1.5 kW, the exergy efficiency trends rise by 70.2% at the membrane area of 5 cm<sup>2</sup> while the increment rate is 62.7% at the area of 75 cm<sup>2</sup> , The ε trends state that the exergy efficiency is higher at the low membrane areas since less exergy destruction rates occurred compared to the larger membrane areas. In the defined range, the maximum ε is obtained as 53.7% whilst the minimum ε is 27.3%.
>
> *[equation E14, page 12 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E14_p12.png)]*
>
> Figures 6A,B present the GOR and PR trends for the DCMD performance assessment, respectively. It is seen that both GOR and PR have the highest values at the minimum membrane area, 5 cm<sup>2</sup> , and the difference between the minimum and maximum membrane areas is huge, namely, the maximum GOR and PR values are nearly 14 times higher than the GOR and PR values of the minimum membrane area. One of the main concerns is the increase of pump power rate (both feed and permeate pumps) when the membrane area increases. However, according to the performance curves of the selected pumps for the hybrid system, the increase of membrane area from 5 to 75 cm<sup>2</sup> does not remarkably affect the pump power rate. It must be noted that the increase of membrane area can affect the pump power rates for larger-scale operations from the viewpoints of membrane area (Am) and DC cooling load (Q<sup>_</sup> DC ), but the current study proposes this hybrid system for the low Q<sup>_</sup> DC values; and therefore, the increase of Am is not a critical consideration for the pump operations. In addition, both GOR and PR grow up by increasing of Q<sup>_</sup> DC . From 0.7 to 1.5 kW, the GOR increases by nearly 33.8% whereas the PR trends reach their 1.9 times higher value.
>
> FIGURE 5 Efficiency of the combined system: A, membrane thermal efficiency and B, overall exergy efficiency [Colour figure can be viewed at wileyonlinelibrary.com]
>
> The sustainability index (SI) trends are shown in Figure 7. It is seen that smaller membrane area and higher Q<sup>_</sup> DC present higher SI trends. For example, the maximum SI is obtained as 2.16 at the membrane area of 5 cm<sup>2</sup> and the released heat of 1.5 kW whilst the minimum SI is calculated as 1.38 at the membrane area of 75 cm<sup>2</sup> and the released heat of 0.7 kW. Also, the SI difference between the membrane areas of 5 and 75 cm<sup>2</sup> increases by rising of the Q<sup>_</sup> DC trends. At 1.5 kW, the smallest membrane area has 20.1% higher SI values than the largest membrane area while this percentage is 6.2% at 0.7 kW. These results deduce the SI has parallel trends with the ε; thus, it can be assessed instead of ε in further studies when the calculation of ε becomes more complex for different hybrid DCMD-DC cooling systems.
>
> FIGURE 6 Energetic performance assessments of the combined system: A, gain output ratio and B, performance ratio [Colour figure can be viewed at wileyonlinelibrary.com]
>
> FIGURE 8 Payback period trends of the combined system [Colour figure can be viewed at wileyonlinelibrary.com]

**Moves:**

**Claims:**

**Meaning:**

---

## Step 18 — 4 | RESULTS AND DISCUSSION (continued) (page 13, ~279 words)

> *[equation E15, page 13 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E15_p13.png)]*
>
> The conventional economic analysis is analyzed with the payback period PP trends in Figure 8. In the operating ranges of the hybrid system, the PP does not show crucial variation and stays stable at roundly 3.72 years that is very smaller than the system lifetime, 20 years. The Q<sup>_</sup> DC does not change the PP values remarkably while the Am has a very small impact as shown in Figure 8. The reason behind the stable trends may be the low cooling loads of the currently proposed hybrid system, and the
>
> Q_ DC may significantly affect the PP at higher DC cooling load operations. Similarly, higher membrane areas can also affect the PP trends more remarkably. Since the current study focused on the low Q<sup>_</sup> DC in the range of 0.7 to 1.5 kW with small Am values between 5 and 75 cm<sup>2</sup> , the PP is assumed constant. Further studies can better analyze the impact of higher Q<sup>_</sup> DC and Am values on the PP calculation.

**Moves:**

**Claims:**

**Meaning:**

---

## Step 19 — 4 | RESULTS AND DISCUSSION (continued) (page 13, ~457 words)

> The levelized cost of the distilled water, C<sup>_</sup> dw , the levelized product cost of the hybrid system, C<sup>_</sup> p , and the levelized cost of the data center cooling, C<sup>_</sup> dc, are analyzed in the thermoeconomic assessments. Figure 9A projects the C<sup>_</sup> dw trends at different Am and Q<sup>_</sup> DC values. Compared to the Q<sup>_</sup> DC , the Am has negligible impacts on the C<sup>_</sup> dw while the C<sup>_</sup> dw increases roundly 1.9 times as high from the Q<sup>_</sup> DC of 0.7 to 1.5 kW. Like C<sup>_</sup> dw, the C<sup>_</sup> p and C<sup>_</sup> dc deduce the same increasing trends; thus, they are not projected in Figure 9A. However, they have different levelized cost values so that their levelized costs are compared to one another at different Q<sup>_</sup> DC , independently from the Am, in Figure 9B. As expected from the nature of the exergy cost matrix in Equation (34), the C<sup>_</sup> p has the highest levelized product cost values since it consists of both DC cooling and DCMD operation. The C<sup>_</sup> dc follows the C<sup>_</sup> p , and the difference between them decreases by rising of the Q<sup>_</sup> DC . For example, the C<sup>_</sup> dc is 2.1% smaller than the C<sup>_</sup> p at the Q_ DC of 0.7 kW whereas it is 1.3% smaller at the Q_ DC of 1.5 kW. Amongst others, the C<sup>_</sup> dw has the lowest values and the reason is the lower capital costs of the DCMD module compared to the total capital cost of the hybrid system and the capital cost of the DC cooling equipment (see Table 2). At the lowest Q<sup>_</sup> DC (0.7 kW), the C<sup>_</sup> dw and C_ dc are very close to each other, namely, C_ dw is 0.68% lower than the C<sup>_</sup> dc . However, by increasing the Q<sup>_</sup> DC , the capital cost of the DC cooling unit rises sharper than the capital cost of the DCMD module; hence, the difference between the C<sup>_</sup> dw and C<sup>_</sup> dc increases and the C<sup>_</sup> dw becomes 6.6% smaller than the C<sup>_</sup> dc . The thermoeconomic assessment shows that the levelized costs dramatically increase with the Q<sup>_</sup> DC increment and the increasing trends are also affected by the exergetic cost values of the system which is considered as the entire hybrid design (C<sup>_</sup> p ), stand-alone DC cooling unit (C<sup>_</sup> dc ), and DCMD module (C<sup>_</sup> dw).
>
> FIGURE 9 Thermoeconomic performance assessments of the hybrid system: A, levelized cost of the distilled water, B, comparative bar chart for the levelized product, distilled water, and data center cooling costs [Colour figure can be viewed at wileyonlinelibrary.com]
>
> FIGURE 10 The best trade-off point selection of the hybrid system with the Pareto frontier plots [Colour figure can be viewed at wileyonlinelibrary.com]

**Moves:**

**Claims:**

**Meaning:**

---

## Step 20 — 4 | RESULTS AND DISCUSSION (continued) (page 14, ~411 words)

> To see the impact of the difference between the C<sup>_</sup> p and C<sup>_</sup> dw on the selection of the best trade-off point step, we perform the multiobjective optimization study for the coupled objective functions of ε −C<sup>_</sup> p and ε −C<sup>_</sup> dw. The C<sup>_</sup> dc is not selected in the multiobjective optimization study, because its performance trends are between the C<sup>_</sup> p and C_ dw trends. Figure 10 projects the Pareto frontier plots for the coupled-objective functions of ε −C<sup>_</sup> p and ε −C<sup>_</sup> dw . As mentioned in the modeling section, the maximization of the exergetic efficiency and the minimization of the levelized cost are aimed; and the weighting percentages of these objectives are considered as 50%. The best tradeoff point (BToP) is found different for these two coupled functions due to the aforementioned levelized cost difference between the C<sup>_</sup> p and C<sup>_</sup> dw . For the coupled-objective function of ε −C<sup>_</sup> p , the BToP is at the Q<sup>_</sup> DC and Am values of 1.1 kW and 5.13 cm<sup>2</sup> whereas the BToP is at the Q<sup>_</sup> DC and Am values of 1.1 kW and 5.19 cm<sup>2</sup> for the coupledobjective function of ε −C<sup>_</sup> dw . The results infer that the Q_ DC is the same for both coupled-objective functions since it has a significant impact on both exergy efficiency and levelized cost performances (see Figures 5B and 9B, respectively); thus, the middle Q<sup>_</sup> DC value is selected in the operating range of Q<sup>_</sup> DC . On the other hand, the optimal Am value is found close to the minimum Am value. The reason is the impact of Am is less than the impact of Q_ DC for both exergy efficiency and levelized cost trends. When the optimal Am values are compared for two different coupled-objectives, the optimal Am value of the ε− C<sup>_</sup> dw (Am = 5.19 cm<sup>2</sup> ) is found slightly greater than the optimal Am value of the ε −C<sup>_</sup> p (Am = 5.13 cm<sup>2</sup> ), because
>
> *[equation E16, page 14 — [image](../../../../outputs/preparation/kanbur_et_al_2020_desalination_integrated_data_center_cooling/images/E16_p14.png)]*
>
> the Am has more dominant impact on the C<sup>_</sup> dw trends while its impact on the C<sup>_</sup> p is less. It is worth reminding that the obtained outcomes are for the low Q<sup>_</sup> DC values, and the BToP trends can give different outcomes for larger Q<sup>_</sup> DC and Am values. Since the main focus of the current study is to propose a hybrid solution for the Q<sup>_</sup> DC values, larger-scale Q<sup>_</sup> DC and Am are not considered in this work.

**Moves:**

**Claims:**

**Meaning:**

---

## Step 21 — 5 | CONCLUSION (page 15, ~610 words)

> A new hybrid membrane distillation-data center cooling system was presented in the study. The two-phase liquidimmersion cooling unit was selected as the data center cooling system. It was the first time combining the desalination unit with the two-phase liquid-immersion cooling operation. The feed water was heated up with the waste heat of the data center. Then, it was sent to the direct contact membrane distillation module for desalination purposes. Besides the economic and thermodynamic assessments, the thermoeconomic assessment was done with a new and unique exergy-cost matrix. The multiobjective optimization was performed according to the exergy efficiency, the levelized product cost, and the distilled water cost terms. Even though the proposed system was designed for a specific data center cooling load, the results can be useful for real-scale operations in future studies. The system was one of the energy-water nexus examples and the mains conclusions are given as follows:
>
> - The released heat rate from the data center crucially increased the DCMD performance parameters such as heat and mass fluxes. Also, compared to the released heat rate of 0.7 kW, the COP performance was found 1.5 times higher at the released heat rate of 1.5 kW.
>
> - The proposed system was able to produce 6.13 kg water in a day with the applied membrane area of 75 cm<sup>2</sup> . The increment of 0.8 kW data center released heat rate grew up the produced water rate 1.85 times.
>
> - The membrane thermal efficiency varied between 50.1% and 64.5% while the overall exergy efficiency was obtained between 27.3% and 53.7%. The membrane thermal efficiency was independent of the membrane area whilst the overall exergy efficiency was drastically affected.
>
> - The sustainability index trends were found in parallel to the exergy efficiency trends. The highest sustainability index value was calculated as 2.16 at the largest data center released heat rate and the minimum membrane area. In the case of complex hybrid designs that can result in difficulties for exergy efficiency calculations, the sustainability index can be used as an alternative assessment criterion.
>
> - The payback period was calculated as 3.72 years in the operating ranges. The proposed hybrid system was found economically feasible for further real-scale demonstrations.
>
> - The released heat from the data center had a dominant impact on the levelized costs of the hybrid system. Due to the lower exergetic costs of the DCMD module, it had the minimum levelized cost amongst the levelized costs of the overall (hybrid) system and the stand-alone DC cooling unit.
>
> - The levelized product cost range of the hybrid design was between 2.69 and 5.33 SGD/h that corresponded to 64.6 and 127.9 SGD in a day.
>
> - The multiobjective optimization study found the optimal data center cooling rate and the membrane area at 1.1 kW and 5.13 cm<sup>2</sup> for the hybrid design, respectively.
>
> In light of the foregoing outcomes, future studies can be directed in two different ways. The first way is the real-scale demonstration of the proposed hybrid design since the thermodynamic, economic, and thermoeconomic results showed satisfying performances. The hybrid system can be efficiently operated for the low data center cooling loads. Therefore, real-scale demonstration studies and relevant system limitations can be focused in future studies. In this step, different membrane characteristics, distillation techniques, or the dielectric liquid types can be investigated. Also, the impact of corrosion and salt deposition on the condenser pipe can be experimentally tested. The second way is the study of the hybrid system for large scale operations. In this way, the impact of large-scale operations can be seen on thermodynamic and thermoeconomic results. The experimental corrosion and salt deposition investigations can be performed for larger-scale operations as well.

**Moves:**

**Claims:**

**Meaning:**

---

## My takeaways


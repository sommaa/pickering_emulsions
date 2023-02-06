<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/grouptwentynine/Pickering_emulsions">
    <img src="https://user-images.githubusercontent.com/120776791/210553577-adba89f7-0708-44ee-bd32-f343b6eb180c.png" alt="Logo" width="350" height="240">
  </a>
      <br />
    <h1 align="center">Pickering emulsions models</h3>
</div>

## Abstract:
The present work gives an insight on Pickering emulsions, which are a particular type of emulsions that uses solid colloidal particles as stabilizers and have gained rising popularity in the past decades thanks to their ability to prevent the droplets from coalescing and their non-toxic behavior. 
A collection of existing mathematical models for the investigation of different aspects regarding this matter is reported in this study, these aspects being: the kinetics of formation of the droplets, and the droplets size.

## Main Codes:
  - [langevin_random.m](https://github.com/sommaa/pickering_emulsions/blob/main/scripts/langevin_random.m): impulse, adapted, constrained langevin integrator;
  - [postprocessing.py](https://github.com/sommaa/pickering_emulsions/blob/main/scripts/postprocessing.py): langevin_random.m blender postprocessor;
  - [size_particle.m](https://github.com/sommaa/pickering_emulsions/blob/main/scripts/size_droplet.m): model for the prediction of the droplet diameter in a pickering emulsion for oppositely charged particles.

## Authors:
- Andrea Somma (Main Coder)
- Elvira Kazimova
- Giovanni Tomaciello
- Giovanni Madella
- Sabrina Ulivelli

## User guide:
Download the whole folder as a .zip file and extract it entirely to let matlab load experimental data tables or clone the repo with:
  ```bash
   $: git clone https://github.com/sommaa/pickering_emulsions.git
  ```
### furthermore:
- [langevin_random.m](https://github.com/sommaa/pickering_emulsions/blob/main/scripts/langevin_random.m) code can take several hours to run correctly, be patient.
- [postprocessing.py](https://github.com/sommaa/pickering_emulsions/blob/main/scripts/postprocessing.py) can be used to postprocess in [blender](https://www.blender.org/) the authomatically written result from [langevin_random.m](https://github.com/sommaa/pickering_emulsions/blob/main/scripts/langevin_random.m).
- Langevin integrator results can be also postprocessed in [paraview](https://www.paraview.org/) importing the .txt files with "Table to points" filter, and using comma as column separator, without headers; then displaying spheres with "glyph" filter.

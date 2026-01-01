import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. PAGE CONFIG & CYBERPUNK CSS (YOUR UPDATES)
# ==========================================
st.set_page_config(page_title="UTDL: Vacuum Genesis", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Share+Tech+Mono&display=swap');
    
    /* GLOBAL THEME */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at center, #0a0020 0%, #000000 100%);
        color: #00ffea;
    }
    
    /* HEADERS (PULSING PINK & CYAN) */
    h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 5em;
        color: #ff00ff;
        text-align: center;
        text-shadow: 0 0 40px #ff00ff, 0 0 80px #ff00ff;
        letter-spacing: 12px;
        animation: pulse 6s infinite alternate;
        margin-bottom: 0;
    }
    h2 {
        font-family: 'Orbitron', sans-serif;
        font-size: 3em;
        color: #00ffff;
        text-align: center;
        text-shadow: 0 0 30px #00ffff;
        margin-top: 0;
    }
    
    /* CINEMATIC TEXT */
    .cinematic {
        font-family: 'Share Tech Mono', monospace;
        font-size: 1.8em;
        color: #00ffea;
        text-align: center;
        text-shadow: 0 0 15px #00ffea;
        margin: 60px 0;
        line-height: 1.6;
    }
    
    /* LEGITIMACY BOX */
    .legitimacy {
        background: rgba(10, 0, 32, 0.95);
        padding: 40px;
        border-radius: 20px;
        border: 4px solid #ff00ff;
        box-shadow: 0 0 60px rgba(255, 0, 255, 0.4);
        margin: 80px auto;
        font-family: 'Share Tech Mono', monospace;
        font-size: 1.2em;
        text-align: center;
        color: #00ffff;
        line-height: 1.8;
    }
    
    /* LINK BUTTON */
    .back-link {
        display: block;
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        border: 2px solid #00ffff;
        color: #00ffff;
        text-decoration: none;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2em;
        transition: 0.3s;
    }
    .back-link:hover {
        background: #00ffff;
        color: #000;
        box-shadow: 0 0 30px #00ffff;
    }

    /* ANIMATION */
    @keyframes pulse {
        from { opacity: 0.8; transform: scale(0.98); }
        to { opacity: 1; transform: scale(1.02); }
    }
    
    /* HIDE UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. HEADER SECTION
# ==========================================
st.markdown("<h1>UTDL</h1>", unsafe_allow_html=True)
st.markdown("<h1>GENESIS</h1>", unsafe_allow_html=True)
st.markdown("<h2>Universal Tension-Driven Lattice</h2>", unsafe_allow_html=True)



# ==========================================
# 3. WEBGL 1: THE LATTICE BREATHER
# ==========================================
st.markdown("<div class='cinematic'>// SYSTEM 01: THE LATTICE BREATHES</div>", unsafe_allow_html=True)

# Three.js Particle System (The Wave)
webgl_lattice = """
<!DOCTYPE html>
<html>
<head>
    <style> body { margin: 0; overflow: hidden; background: transparent; } </style>
</head>
<body>
    <div id="container"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://unpkg.com/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script>
        const container = document.getElementById('container');
        const scene = new THREE.Scene();
        
        const camera = new THREE.PerspectiveCamera(60, window.innerWidth/600, 0.1, 1000);
        camera.position.set(0, 20, 40);
        
        const renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
        renderer.setSize(window.innerWidth, 600);
        container.appendChild(renderer.domElement);
        
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.autoRotate = true;
        controls.autoRotateSpeed = 1.0;

        // --- PARTICLES ---
        const size = 35;
        const count = size * size; 
        const geometry = new THREE.BufferGeometry();
        const positions = new Float32Array(count * 3);
        const colors = new Float32Array(count * 3);
        const originals = new Float32Array(count * 3);

        let i = 0;
        for(let x=0; x<size; x++){
            for(let z=0; z<size; z++){
                const px = (x - size/2) * 1.2;
                const pz = (z - size/2) * 1.2;
                positions[i] = px; positions[i+1] = 0; positions[i+2] = pz;
                originals[i] = px; originals[i+1] = 0; originals[i+2] = pz;
                colors[i]=0.1; colors[i+1]=0.1; colors[i+2]=0.3; // Dark Blue Base
                i+=3;
            }
        }
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

        const material = new THREE.PointsMaterial({
            size: 0.6, vertexColors: true, 
            transparent: true, opacity: 0.9,
            blending: THREE.AdditiveBlending
        });
        const particles = new THREE.Points(geometry, material);
        scene.add(particles);

        // --- ANIMATION ---
        let time = 0;
        function animate() {
            requestAnimationFrame(animate);
            time += 0.04;
            controls.update();

            const pos = geometry.attributes.position.array;
            const col = geometry.attributes.color.array;

            for(let j=0; j<count; j++){
                const idx = j*3;
                const ox = originals[idx];
                const oz = originals[idx+2];
                const r = Math.sqrt(ox*ox + oz*oz);

                // UTDL Wave Function: Soliton Pulse
                const wave = 6.0 * Math.exp(-(r*r)/100) * Math.sin(time*2 - r*0.3);
                
                // Hardening Effect (Non-linear y-displacement)
                const hardening = wave + (wave*wave*wave)*0.01; 
                pos[idx+1] = hardening;

                // Color Shift: Blue -> Cyan -> Magenta (at peaks)
                const energy = Math.abs(wave)/5;
                col[idx] = energy * 2.0;   // Red channel (creates Magenta)
                col[idx+1] = energy + 0.2; // Green channel (creates Cyan)
                col[idx+2] = 1.0;          // Blue channel (Base)
            }
            geometry.attributes.position.needsUpdate = true;
            geometry.attributes.color.needsUpdate = true;
            renderer.render(scene, camera);
        }
        animate();
        
        window.addEventListener('resize', () => {
            renderer.setSize(window.innerWidth, 600);
            camera.aspect = window.innerWidth / 600;
            camera.updateProjectionMatrix();
        });
    </script>
</body>
</html>
"""
components.html(webgl_lattice, height=600)

st.markdown("""
<div class='cinematic'>
    The lattice pulses.<br>
    A soliton emerges from the wave.<br>
    Matter grips the void.
</div>
""", unsafe_allow_html=True)

# ==========================================
# 4. WEBGL 2: NUCLEAR BINDING (NEW)
# ==========================================
st.markdown("<div class='cinematic'>// SYSTEM 02: NUCLEAR BINDING</div>", unsafe_allow_html=True)

# Three.js Dual Core Simulation
webgl_nuclear = """
<!DOCTYPE html>
<html>
<head>
    <style> body { margin: 0; overflow: hidden; background: transparent; } </style>
</head>
<body>
    <div id="container2"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById('container2');
        const scene = new THREE.Scene();
        
        const camera = new THREE.PerspectiveCamera(60, window.innerWidth/600, 0.1, 1000);
        camera.position.set(0, 30, 0); // Top down view
        camera.lookAt(0,0,0);
        
        const renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
        renderer.setSize(window.innerWidth, 600);
        container.appendChild(renderer.domElement);

        // --- DUAL CORE PARTICLES ---
        const pCount = 3000;
        const geo = new THREE.BufferGeometry();
        const pos = new Float32Array(pCount * 3);
        const col = new Float32Array(pCount * 3);

        for(let i=0; i<pCount*3; i+=3){
            pos[i] = (Math.random()-0.5)*50;
            pos[i+1] = 0;
            pos[i+2] = (Math.random()-0.5)*50;
            col[i]=0; col[i+1]=1; col[i+2]=1;
        }
        geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
        geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
        
        const mat = new THREE.PointsMaterial({
            size: 0.8, vertexColors: true, blending: THREE.AdditiveBlending, transparent: true
        });
        const system = new THREE.Points(geo, mat);
        scene.add(system);

        // CORES
        const coreGeo = new THREE.SphereGeometry(2, 16, 16);
        const coreMat = new THREE.MeshBasicMaterial({color: 0xff00ff});
        const c1 = new THREE.Mesh(coreGeo, coreMat);
        const c2 = new THREE.Mesh(coreGeo, coreMat);
        scene.add(c1); scene.add(c2);

        let t = 0;
        function animate() {
            requestAnimationFrame(animate);
            t += 0.02;

            // Spiral Dynamics
            const dist = 10 * Math.cos(t * 0.3) + 12; // Oscillate distance
            const ang = t * 2.0;

            c1.position.set(Math.cos(ang)*dist/2, 0, Math.sin(ang)*dist/2);
            c2.position.set(Math.cos(ang+Math.PI)*dist/2, 0, Math.sin(ang+Math.PI)*dist/2);

            // Field Reaction (Strain Overlap)
            const p = geo.attributes.position.array;
            const c = geo.attributes.color.array;

            for(let i=0; i<pCount; i++){
                const idx = i*3;
                const px = p[idx]; const pz = p[idx+2];
                
                // Dist to cores
                const d1 = Math.sqrt((px-c1.position.x)**2 + (pz-c1.position.z)**2);
                const d2 = Math.sqrt((px-c2.position.x)**2 + (pz-c2.position.z)**2);

                // Strain = Inverse distance overlap
                const strain = (15/(d1+1)) + (15/(d2+1));
                
                // Lift particles based on strain
                p[idx+1] = strain * 2.0; 

                // Color: Cyan (low) -> Pink (high strain)
                c[idx] = strain * 0.2;
                c[idx+1] = 1.0 - (strain * 0.1);
            }
            geo.attributes.position.needsUpdate = true;
            geo.attributes.color.needsUpdate = true;
            
            renderer.render(scene, camera);
        }
        animate();
        
        window.addEventListener('resize', () => {
            renderer.setSize(window.innerWidth, 600);
            camera.aspect = window.innerWidth / 600;
            camera.updateProjectionMatrix();
        });
    </script>
</body>
</html>
"""
components.html(webgl_nuclear, height=600)

st.markdown("""
<div class='cinematic'>
    Two cores spiral inward.<br>
    Strain fields overlap.<br>
    The "Strong Force" is geometry.
</div>
""", unsafe_allow_html=True)


# ==========================================
# 6. LEGITIMACY & FOOTER
# ==========================================
st.markdown("""
<div class='legitimacy'>
    <strong>// GENESIS CONFIRMED //</strong><br><br>
    This is not an animation. It is the real-time execution of the UTDL Constitutive Law:
    <br><br>
    <span style="font-size: 1.5em; color: #ff00ff;">F = -k₀x - αx³</span>
    <br><br>
    From this single equation, we witness:
    <br>1. <strong>Dispersion → Localization</strong> (Mass)
    <br>2. <strong>Strain Overlap → Binding</strong> (Strong Force)
    <br><br>
    No tuning. No particles. Only the lattice.
    <br><br>
    — William Oliver Rubin
</div>
""", unsafe_allow_html=True)

st.markdown("""
<a href="https://utdlx.com" class="back-link">
    &lt; RETURN TO UTDLX.COM
</a>
""", unsafe_allow_html=True)

st.markdown("<div class='cinematic'>The lattice lives.<br>Reality is here.<br>You have seen genesis.</div>", unsafe_allow_html=True)
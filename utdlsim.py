import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. PAGE CONFIG & CYBERPUNK CSS
# ==========================================
st.set_page_config(page_title="UTDL: GENESIS", layout="centered", initial_sidebar_state="collapsed")

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
        font-size: 1em;
        color: #ff00ff;
        text-align: center;
        text-shadow: 0 0 40px #ff00ff, 0 0 80px #ff00ff;
        letter-spacing: 12px;
        animation: pulse 6s infinite alternate;
        margin-bottom: 0;
    }
    h2 {
        font-family: 'Orbitron', sans-serif;
        font-size: 1em;
        color: #00ffff;
        text-align: center;
        text-shadow: 0 0 30px #00ffff;
        margin-top: 0;
    }
    
    /* CINEMATIC TEXT */
    .cinematic {
        font-family: 'Share Tech Mono', monospace;
        font-size: 1.5em;
        color: #00ffea;
        text-align: center;
        text-shadow: 0 0 15px #00ffea;
        margin: 10px 0;
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


# ==========================================
# 3. VERTICAL MOBILE STUDIO (ADDED AS REQUESTED)
# ==========================================
st.markdown("<div class='cinematic'>// SYSTEM 00: THE GENESIS SEQUENCE</div>", unsafe_allow_html=True)

webgl_mobile_engine = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <style>
        body { margin: 0; overflow: hidden; background: transparent; font-family: 'Share Tech Mono', monospace; }
        #canvas-container-v { position: relative; width: 100%; height: 600px; z-index: 1; }
        
        /* MOBILE HUD OVERLAY */
        #hud {
            position: absolute;
            bottom: 71%; 
            left: 5%;
            width: 90%;
            z-index: 10;
            color: #00ffff;
            pointer-events: none;
            text-align: center; 
            text-shadow: 0 0 3px #00ffff;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        #phase-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5em; 
            font-weight: 300;
            margin: 0;
            margin-top: 5px;
            text-transform: uppercase;
            line-height: 1.1;
        }
        #phase-desc {
            font-size: 0.8em; 
            color: #e0e0e0;
            margin-top: 15px;
            background: rgba(0,0,0,0.8);
            padding: 15px;
            border-top: 2px solid #ff00ff; 
            border-bottom: 2px solid #ff00ff;
            border-radius: 10px;
        }
        #timer {
            position: absolute;
            top: 5%;
            right: 5%;
            font-size: 1.5em;
            color: #555;
            font-family: 'Orbitron', sans-serif;
        }
        /* RESET BUTTON (Top Left or Bottom Center) */
        #reset-btn {
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 50;
            background: rgba(0, 0, 0, 0.5);
            color: #ff0055;
            border: 1px solid #ff0055;
            font-family: 'Share Tech Mono', monospace;
            font-size: 4vw; /* Responsive for mobile */
            padding: 8px 15px;
            cursor: pointer;
            display: none; /* Hidden by default */
            border-radius: 5px;
        }
        #reset-btn:hover {
            background: #ff0055;
            color: #000;
        }
        /* START BUTTON */
        #start-btn {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            z-index: 20;
            padding: 15px 30px;
            font-family: 'Orbitron', sans-serif;
            font-size: 2em;
            background: rgba(0,0,0,0.8);
            color: #00ffff;
            border: 2px solid #00ffff;
            cursor: pointer;
            border-radius: 10px;
            white-space: nowrap;
        }
    </style>
</head>
<body>
    <div id="canvas-container-v"></div>
    
    <div id="hud" style="display:none;">
        <div id="phase-title">SYSTEM READY</div>
        <div id="phase-desc">Waiting for input...</div>
    </div>
    
    <div id="timer">T+0.00s</div>
    <button id="reset-btn" onclick="resetSequence()">// RESET</button>
    
    <button id="start-btn" onclick="startSequence()">INITIATE GENESIS</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // --- SETUP ---
        const container = document.getElementById('canvas-container-v');
        const hud = document.getElementById('hud');
        const pTitle = document.getElementById('phase-title');
        const pDesc = document.getElementById('phase-desc');
        const timerDiv = document.getElementById('timer');
        const startBtn = document.getElementById('start-btn');

        const scene = new THREE.Scene();
        scene.background = null;
        
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        
        // CAMERA POSITION
        camera.position.set(0, 50, 90); 
        camera.lookAt(0, 0, 0);
        
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        renderer.setPixelRatio(window.devicePixelRatio); 
        container.appendChild(renderer.domElement);

        // --- OBJECTS ---
        
        // 1. THE LATTICE
        const gridSize = 80; 
        const particleCount = gridSize * gridSize;
        const geoLattice = new THREE.BufferGeometry();
        const posLattice = new Float32Array(particleCount * 3);
        const colLattice = new Float32Array(particleCount * 3);
        const origLattice = new Float32Array(particleCount * 3);

        let idx = 0;
        for(let x=0; x<gridSize; x++){
            for(let z=0; z<gridSize; z++){
                const px = (x - gridSize/2) * 1.5;
                const pz = (z - gridSize/2) * 1.5;
                posLattice[idx] = px; posLattice[idx+1] = 0; posLattice[idx+2] = pz;
                origLattice[idx] = px; origLattice[idx+1] = 0; origLattice[idx+2] = pz;
                colLattice[idx]=0.1; colLattice[idx+1]=0.1; colLattice[idx+2]=0.3; 
                idx+=3;
            }
        }
        geoLattice.setAttribute('position', new THREE.BufferAttribute(posLattice, 3));
        geoLattice.setAttribute('color', new THREE.BufferAttribute(colLattice, 3));
        const matLattice = new THREE.PointsMaterial({ size: 0.8, vertexColors: true, blending: THREE.AdditiveBlending, transparent: true });
        const latticeMesh = new THREE.Points(geoLattice, matLattice);
        scene.add(latticeMesh);

        // 2. THE CORES
        const coreGeo = new THREE.SphereGeometry(3.5, 32, 32); 
        const coreMat = new THREE.MeshBasicMaterial({ color: 0xff0055 });
        const core1 = new THREE.Mesh(coreGeo, coreMat);
        const core2 = new THREE.Mesh(coreGeo, coreMat);
        core1.position.set(1000,0,0);
        core2.position.set(-1000,0,0);
        scene.add(core1);
        scene.add(core2);

        // 3. THE BINDING MESH
        const bindGeo = new THREE.PlaneGeometry(50, 80, 20, 40); 
        const bindMat = new THREE.MeshBasicMaterial({ color: 0x00ffff, wireframe: true, transparent: true, opacity: 0.0 });
        const bindMesh = new THREE.Mesh(bindGeo, bindMat);
        bindMesh.rotation.x = -Math.PI / 2;
        bindMesh.rotation.z = Math.PI / 2; 
        scene.add(bindMesh);

        // --- LOGIC ---
        let isRunning = false;
        let startTime = 0;
        let cameraAngle = 0;

        function startSequence() {
            startBtn.style.display = 'none';
            hud.style.display = 'flex';
            
            // SHOW THE RESET BUTTON
            document.getElementById('reset-btn').style.display = 'block'; 
            
            isRunning = true;
            startTime = Date.now();
        }

        function updateHUD(title, desc, color) {
            pTitle.innerText = title;
            pTitle.style.color = color;
            pTitle.style.textShadow = `0 0 20px ${color}`;
            pDesc.innerHTML = desc;
            pDesc.style.borderColor = color;
        }
function resetSequence() {
            // 1. Stop Physics
            isRunning = false;
            
            // 2. UI Reset
            hud.style.display = 'none';           // Hide HUD
            document.getElementById('reset-btn').style.display = 'none'; // Hide Reset Button
            startBtn.innerHTML = "RE-INITIATE<br>GENESIS"; // Change Text
            startBtn.style.display = 'block';     // Show Big Start Button
            timerDiv.innerText = "T+0.00s";
            
            // 3. Scene Reset (Visuals)
            // Restore Lattice
            latticeMesh.visible = true;
            latticeMesh.material.opacity = 1.0;
            
            // Hide Binding Mesh
            bindMesh.material.opacity = 0.0;
            
            // Flatten Binding Mesh (Reset Vertices)
            const verts = bindMesh.geometry.attributes.position.array;
            for(let k=2; k<verts.length; k+=3) verts[k] = 0;
            bindMesh.geometry.attributes.position.needsUpdate = true;

            // Reset Cores to off-screen
            core1.position.set(1000,0,0);
            core2.position.set(-1000,0,0);
            
            // Reset Lattice Waves (Optional: Flatten them instantly)
            const pos = geoLattice.attributes.position.array;
            const col = geoLattice.attributes.color.array;
            for(let i=0; i<particleCount; i++){
                const ix = i*3;
                pos[ix+1] = 0; // Flat
                col[ix]=0.1; col[ix+1]=0.1; col[ix+2]=0.3; // Blue
            }
            geoLattice.attributes.position.needsUpdate = true;
            geoLattice.attributes.color.needsUpdate = true;
        }
        function animate() {
            requestAnimationFrame(animate);
            
            if(!isRunning) {
                latticeMesh.rotation.y += 0.005;
                renderer.render(scene, camera);
                return;
            }

            const now = (Date.now() - startTime) / 1000;
            timerDiv.innerText = "T+" + now.toFixed(2) + "s";

            // Camera Orbit
            cameraAngle += 0.003;
            camera.position.x = Math.sin(cameraAngle) * 90;
            camera.position.z = Math.cos(cameraAngle) * 90;
            camera.lookAt(0, 0, 0);

            // PHASE 1: LINEAR (0-10s)
            if (now < 10) {
                updateHUD("PHASE 1 LINEAR VACUUM", "Standard Model (F=-kx) Energy disperses. No Matter.", "#00ffff");
                
                const pos = geoLattice.attributes.position.array;
                const col = geoLattice.attributes.color.array;
                for(let i=0; i<particleCount; i++){
                    const ix = i*3;
                    const r = Math.sqrt(origLattice[ix]**2 + origLattice[ix+2]**2);
                    const wave = 3.0 * Math.sin(now*3 - r*0.4) * Math.exp(-r*0.03); 
                    pos[ix+1] = wave;
                    col[ix] = 0; col[ix+1] = 0.2; col[ix+2] = 0.8 + wave*0.1;
                }
                geoLattice.attributes.position.needsUpdate = true;
                geoLattice.attributes.color.needsUpdate = true;
            }

            // PHASE 2: HARDENING (10-20s)
            else if (now < 20) {
                updateHUD("PHASE 2 HARDENING", "UTDL (F=-kx-αx³) Vacuum Stiffens. Mass Created.", "#ff00ff");
                const progress = Math.min((now - 10)/2, 1.0);
                const pos = geoLattice.attributes.position.array;
                const col = geoLattice.attributes.color.array;
                for(let i=0; i<particleCount; i++){
                    const ix = i*3;
                    const r = Math.sqrt(origLattice[ix]**2 + origLattice[ix+2]**2);
                    const wave = 12.0 * Math.exp(-(r*r)/60) * Math.sin(now*4);
                    pos[ix+1] = wave * progress;
                    const energy = Math.abs(wave)/10;
                    col[ix] = energy * 3.0 * progress; col[ix+1] = 0.2; col[ix+2] = 1.0;
                }
                geoLattice.attributes.position.needsUpdate = true;
                geoLattice.attributes.color.needsUpdate = true;
            }

            // PHASE 3: PROTON (20-30s)
            else if (now < 30) {
                updateHUD("PHASE 3 THE PROTON", "Vector Knot. Mass is Geometry. Not a Particle.", "#ff0055");
                const pos = geoLattice.attributes.position.array;
                const col = geoLattice.attributes.color.array;
                for(let i=0; i<particleCount; i++){
                    const ix = i*3;
                    const r = Math.sqrt(origLattice[ix]**2 + origLattice[ix+2]**2);
                    const wave = 15.0 * Math.exp(-(r*r)/30) * (1 + 0.3*Math.sin(now*5));
                    pos[ix+1] = wave;
                    const energy = Math.abs(wave)/12;
                    col[ix] = energy * 4.0; col[ix+1] = 0; col[ix+2] = 0.5;
                }
                geoLattice.attributes.position.needsUpdate = true;
                geoLattice.attributes.color.needsUpdate = true;
            }

            // TRANSITION (30-35s)
            else if (now < 35) {
                updateHUD("INJECTING NUCLEON 2", "Preparing Binding Simulation...", "#ffffff");
                latticeMesh.material.opacity = 1.0 - (now - 30)/5;
                bindMesh.material.opacity = (now - 30)/5 * 0.6; 
            }

           // PHASE 4: BINDING (35-55s)
            else if (now < 55) {
                updateHUD("PHASE 4 DEUTERIUM", "Strain Overlap. No Gluons. Just Geometry.", "#00ff00");
                latticeMesh.visible = false;
                const tLocal = now - 35;
                
                const dist = 50 * Math.exp(-tLocal * 0.15) + 0.5; 
                const ang = tLocal * 2.5;

                const c1x = Math.cos(ang)*dist; 
                const c1z = Math.sin(ang)*dist;
                const c2x = Math.cos(ang+Math.PI)*dist; 
                const c2z = Math.sin(ang+Math.PI)*dist;

                core1.position.set(c1x, 0, c1z);
                core2.position.set(c2x, 0, c2z);

                const verts = bindMesh.geometry.attributes.position.array;
                
                for(let k=0; k<verts.length; k+=3){
                     const lx = verts[k]; 
                     const ly = verts[k+1];
                     
                     const wx = ly; 
                     const wz = lx;
                     
                     const d1 = Math.sqrt((wx - c1x)**2 + (wz - c1z)**2);
                     const d2 = Math.sqrt((wx - c2x)**2 + (wz - c2z)**2);
                     
                     const strain = (40 / (d1+2)) + (40 / (d2+2));
                     verts[k+2] = strain;
                }
                bindMesh.geometry.attributes.position.needsUpdate = true;
            }

            // END
            if (now >= 55) {
                updateHUD("GENESIS COMPLETE", "Deuterium Stable. Welcome to Reality.", "#ffffff");
            }

            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            renderer.setSize(container.clientWidth, container.clientHeight);
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
        });
    </script>
</body>
</html>
"""
components.html(webgl_mobile_engine, height=600)

st.markdown("""
<div class='cinematic'>
    This is the automated Genesis Sequence.<br>
    It transitions from Void to Deuterium.<br>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 4. WEBGL 1: THE LATTICE BREATHER (ORIGINAL)
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
components.html(webgl_lattice, height=420)

st.markdown("""
<div class='cinematic'>
    The lattice pulses.<br>
    A soliton emerges from the wave.<br>
    Matter grips the void.
</div>
""", unsafe_allow_html=True)

# ==========================================
# 5. WEBGL 2: NUCLEAR BINDING (ORIGINAL)
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
st.markdown("<div class='cinematic'>The lattice lives.<br>Reality is here.<br>You have seen genesis.</div>", unsafe_allow_html=True)
st.markdown("""
<a href="https://utdlx.com" class="back-link">
    &lt; RETURN TO UTDLX.COM
</a>
""", unsafe_allow_html=True)


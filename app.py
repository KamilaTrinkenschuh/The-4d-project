import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Hello 4d", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_coding = load_lottieurl("https://lottie.host/8c635b79-ce29-4aa2-ac28-b25685e66215/sUaaoqnSlC.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Welcome on my website :tada:")
    st.title("In the following article you will read some very inspiring things about the 4th dimension!")
    
    st.write("[Tesseract animation Video made with blender >]https://www.youtube.com/watch?v=3hlHGWJD2Fw")
    st.write("""
        I made a blender animation of a rotating tessaract. Check it out!""")
    

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("1.) What is a tessaract?")
        st.write("##")
        st.write(
            """
            In geometry, a tesseract is the four-dimensional analogue of the cube; the tesseract is to the cube as the cube is to the square. Just as the surface of the cube consists of six square faces, the hypersurface of the tesseract consists of eight cubical cells. The tesseract is one of the six convex regular 4-polytopes.

            The tesseract is also called an 8-cell, C8, (regular) octachoron, octahedroid, cubic prism, and tetracube. It is the four-dimensional hypercube, or 4-cube as a member of the dimensional family of hypercubes or measure polytopes. Coxeter labels it the 

            The term hypercube without a dimension reference is frequently treated as a synonym for this specific polytope.

            The Oxford English Dictionary traces the word tesseract to Charles Howard Hinton's 1888 book A New Era of Thought. The term derives from the Greek téssara (τέσσαρα 'four') and from aktís (ἀκτίς 'ray'), referring to the four edges from each vertex to other vertices. Hinton originally spelled the word as tessaract.
        """)
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")
    

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("2.) Geometry")
    st.write("##")

    
    
    st.write(
            """
            As a regular polytope with three cubes folded together around every edge, it has Schläfli symbol {4,3,3} with hyperoctahedral symmetry of order 384. Constructed as a 4D hyperprism made of two parallel cubes, it can be named as a composite Schläfli symbol {4,3} × { }, with symmetry order 96. As a 4-4 duoprism, a Cartesian product of two squares, it can be named by a composite Schläfli symbol {4}×{4}, with symmetry order 64. As an orthotope it can be represented by composite Schläfli symbol { } × { } × { } × { } or { }4, with symmetry order 16.

            Since each vertex of a tesseract is adjacent to four edges, the vertex figure of the tesseract is a regular tetrahedron. The dual polytope of the tesseract is the 16-cell with Schläfli symbol {3,3,4}, with which it can be combined to form the compound of tesseract and 16-cell.

            Each edge of a regular tesseract is of the same length. This is of interest when using tesseracts as the basis for a network topology to link multiple processors in parallel computing: the distance between two nodes is at most 4 and there are many different paths to allow weight balancing.
            """
        )
    st.subheader("Coordinates")
    st.write(
            """
            The standard tesseract in Euclidean 4-space is given as the convex hull of the points (±1, ±1, ±1, ±1). That is, it consists of the points:
            In this Cartesian frame of reference, the tesseract has radius 2 and is bounded by eight hyperplanes (xi = ±1). Each pair of non-parallel hyperplanes intersects to form 24 square faces in a tesseract. Three cubes and three squares intersect at each edge. There are four cubes, six squares, and four edges meeting at every vertex. All in all, it consists of 8 cubes, 24 squares, 32 edges, and 16 vertices.

            """
        )
        
    
    st.subheader("Net")
    st.write(
            """
            An unfolding of a polytope is called a net. There are 261 distinct nets of the tesseract.[7] The unfoldings of the tesseract can be counted by mapping the nets to paired trees (a tree together with a perfect matching in its complement) """
        )
    st.subheader("Construction")
    st.write(
            """

            The construction of hypercubes can be imagined the following way:

1-dimensional: Two points A and B can be connected to become a line, giving a new line segment AB.
2-dimensional: Two parallel line segments AB and CD separated by a distance of AB can be connected to become a square, with the corners marked as ABCD.
3-dimensional: Two parallel squares ABCD and EFGH separated by a distance of AB can be connected to become a cube, with the corners marked as ABCDEFGH.
4-dimensional: Two parallel cubes ABCDEFGH and IJKLMNOP separated by a distance of AB can be connected to become a tesseract, with the corners marked as ABCDEFGHIJKLMNOP. However, this parallel positioning of two cubes such that their 8 corresponding pairs of vertices are each separated by a distance of AB can only be achieved in a space of 4 or more dimensions.
            """ )
    st.subheader("Sources")
    st.write("[Wikipedia >]https://en.wikipedia.org/wiki/Tesseract")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/trinkenschuhkamila@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
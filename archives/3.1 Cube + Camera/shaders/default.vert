#version 330 core

layout (location = 0) in vec3 in_position;

uniform mat4 m_proj; // Créer une variable matrix de 4 par 4

void main() {
    // On change la position en fonction de notre variable
    // On va changer la position pour être en peu plus en arrière :
    gl_Position = m_proj * vec4(in_position.xy, in_position.z - 4.5, 1.0);
}
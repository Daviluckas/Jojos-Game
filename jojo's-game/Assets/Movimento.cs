using UnityEngine;
using System.Collections;

public class Movimento : MonoBehaviour{
    
    public Animator Animacao;
    public bool Chao;
    public LayerMask LayerChao;
    public GameObject Chao2;

    void Start(){

    }

    void Update(){
        Animacao = gameObject.GetComponent<Animator>();
        Chao = Physics2D.OverlapCircle (Chao2.transform.position, 0.1f, LayerChao);


        if(Input.GetAxisRaw("A") == 1) {
            Animacao.SetBool("Walking(a)", true);
            gameObject.transform.Translate(new Vector2 (-0.1f, 0));
        }
            
        if(Input.GetAxisRaw("A") == 0) {
            Animacao.SetBool("Walking(a)", false);
        }

        if(Input.GetAxisRaw("D") == 1) {
            Animacao.SetBool("Walking(d)", true);
            gameObject.transform.Translate(new Vector2 (0.1f, 0));
        }
            
        if(Input.GetAxisRaw("D") == 0) {
            Animacao.SetBool("Walking(d)", false);
        }

        if (Input.GetKeyDown(KeyCode.Space) && Chao){
            Animacao.SetBool("Walking(space)", true);
            GetComponent<Rigidbody2D>().AddForce(new Vector2(0, 700), ForceMode2D.Impulse);
        }

        if(Input.GetMouseButton(0)){
            Animacao.SetBool("Attack", true);
        }
        else{
            Animacao.SetBool("Attack", false);
        }
            
        if(Chao == true) {
            Animacao.SetBool("Walking(space)", !Chao);
        }
    }
}

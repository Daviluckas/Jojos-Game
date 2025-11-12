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
        Chao = Physics2D.OverlapCircle (Chao2.transform.position, 2f, LayerChao);


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

        if(Input.GetAxisRaw("Space") == 1) {
            Animacao.SetBool("Walking(space)", true);
            if(Chao == true){
                gameObject.GetComponent<Rigidbody2D>().AddForce(new Vector2(0, 400));
            }
        }
            
        if(Chao == true) {
            Animacao.SetBool("Walking(space)", false);
        }

        if(Chao == true){
            gameObject.GetComponent<Rigidbody2D> ().AddForce (new Vector2 (0, -1));
        }
    }
}

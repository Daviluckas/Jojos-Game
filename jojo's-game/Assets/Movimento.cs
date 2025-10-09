using UnityEngine;

public class Movimento : MonoBehaviour
{
    public Animator Animacao;

    void Start()
    {
        Animacao = GetComponent<Animator>();
    }

    void Update()
    {
        float movimento = Input.GetAxisRaw("Horizontal");

        if (movimento != 0)
        {
            Animacao.SetBool("Andar", true);
            gameObject.transform.Translate(new Vector2 (-0.1f, 0));
        }
        else
        {
            Animacao.SetBool("Andar", false);
        }
    }
}

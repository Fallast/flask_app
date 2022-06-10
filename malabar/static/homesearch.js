const cols = document.getElementsByClassName("product-col"); 
const titulos = document.getElementsByClassName("product-title");
const data = [];

const relev = ["tablas", "ropa", "otros"];

//llenar data con pares de titulos y sus columnas
for(i = 0; i < cols.length; i++)
{
   data.push({titulo: titulos[i].textContent, categories: prod_categories[i], col: cols[i], id: i});
}

const search = document.getElementById('search');
let search_term = '';

//borrador de acentos
function toNormalForm(str) {
   return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

const scrollToTop = () => {
   const c = document.documentElement.scrollTop || document.body.scrollTop;
   window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
};

//function submatching(search, title){
   //var possible_substring = [];
   //var matching = false;
   //for(i = 0; i < search.length; i++)
      //possible_substring.push(search.slice(0, i+1));

   //console.log(possible_substring);

   //for(i = 0; i < possible_substring.length && !matching; i++)
      //if(possible_substring[i].includes(title))
         //matching = true;
   
   //return matching;
//}

function clearSearch(){
   data.forEach(e => {
      e.col.style.display = "block";
      e.col.parentNode.appendChild(e.col);
   });
}

search.addEventListener('input', (event) => {
   setTimeout(function () { window.scrollTo(0, 0); },2);
   search_term = toNormalForm(event.target.value.toLowerCase());
   if (search_term.length > 0)
      for(x in relev)
         data.forEach(e => {
            if(e.categories.includes(relev[x]))
            {
               if(e.titulo.toLowerCase().includes(search_term))
               {
                  e.col.parentNode.appendChild(e.col);
                  e.col.style.display = "block";
               }
               else
                  e.col.style.display = "none";
            }
         });
   else
      clearSearch();
});

$(function(){
   $(".cat li a").click(function(){
      $(".category").html($(this).html());
      filter = $(".category").html().toLowerCase();
      if(filter == 'todo')
         clearSearch();
      else
         data.forEach(e =>{
            if(e.categories.includes(filter))
               e.col.style.display = "block";
            else
               e.col.style.display = "none";
         })
   })
})

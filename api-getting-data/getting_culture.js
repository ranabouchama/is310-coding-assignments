// api PoetryDB <author>/<Shakespeare>[..][/<lines>][,<title>][..][.<.json>]

async function suggestEntity() {
  try {
    const params = new URLSearchParams({
      text: 'Shakespeare',
      TYPE: 'agent'
    });

    const response = await fetch(`https://www.europeana.eu/api/entity/suggest?${params}`);
    const data = await response.json();
    
    console.log('Shakespeare', data);
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

suggestEntity();
